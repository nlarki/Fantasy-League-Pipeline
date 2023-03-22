from pathlib import Path
import os
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials


@task(retries=3)
def fetchData(dataset_url: str):
    print(dataset_url)
    df = pd.read_csv(dataset_url)
    return df


@task()
def cleanData(df: pd.DataFrame, yearOne: int, yearTwo: int):
    df["cost"] = df["now_cost"]/10
    df["fullname"] =df["first_name"] + " " + df["second_name"]
    #creating a list of all columns that i want to keep in finalised dataset
    final_table_columns = ["fullname","goals_scored","assists","total_points","minutes",
                           "goals_conceded","creativity","influence","threat","bonus","bps","ict_index",
                           "clean_sheets","red_cards","yellow_cards","selected_by_percent","cost",
                           "element_type","team_code"]

    df.drop(columns=[col for col in df if col not in final_table_columns], inplace=True)
    #create a column to specify what season the data is for and to convert cost to correct values
    df["Season"] = f"20{yearOne}-{yearTwo}"
    print(f"columns: {df.dtypes}")
    print(f"rows: {len(df)}")
    return df

@task() #create path if it doesnt exist and load all data into it
def write_local(df: pd.DataFrame, yearOne: int, yearTwo: int, dataName: str):
    Path(f"player_data").mkdir(parents=True, exist_ok=True)
    path = Path(f"player_data/{dataName}_20{yearOne}-{yearTwo}.parquet")
    df.to_parquet(path)
    print(path)
    return path

@task() #write to gcs bucket using prefect blocks
def write_gcs(path: Path):
    #doing this as path object keeps windows path, which causes issues when writing to GCS
    newPath = str(path)
    newPath = newPath.replace("\\", "/")
    gcp_cloud_storage_bucket_block = GcsBucket.load("fpl-gcs")
    gcp_cloud_storage_bucket_block.upload_from_path(from_path=path, to_path=newPath, timeout=(10,200))
    return

@task
def write_bq(df: pd.DataFrame):
    gcp_credentials_block = GcpCredentials.load("fplcreds")

    df.to_gbq(
        destination_table="raw_players.players",
        project_id="formidable-fort-375708",
        credentials=gcp_credentials_block.get_credentials_from_service_account(),
        if_exists="append"
    )



@flow()
def testing(yearOne: int, yearTwo: int):
    dataset_url = f"https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/20{yearOne}-{yearTwo}/players_raw.csv"
    dataName = "raw_players"

    df = fetchData(dataset_url)
    clean = cleanData(df, yearOne, yearTwo)
    path = write_local(clean, yearOne, yearTwo, dataName)
    write_gcs(path)
    write_bq(clean)
    
    # write_gcs(path)

@flow() #loop through all possible years of data
def etl_parent_flow(yr:list[int], yrs:list[int]):
    for y, x in zip(yr,yrs):
        testing(y,x)




if __name__ == "__main__":
    yr = [16,17,18,19,20,21,22]
    yrs = [17,18,19,20,21,22,23]
    etl_parent_flow(yr,yrs)