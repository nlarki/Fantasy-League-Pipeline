from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket


@task(retries=3)
def fetchData(dataset_url: str):
    print(dataset_url)
    df = pd.read_csv(dataset_url)
    return df


@task()
def cleanData(df, yearOne: int, yearTwo: int):
    #creating a list of all columns that i want to keep in finalised dataset
    final_table_columns = ["first_name","second_name","goals_scored","assists","total_points,minutes",
                           "goals_conceded","creativity","influence","threat","bonus","bps","ict_index",
                           "clean_sheets","red_cards","yellow_cards","selected_by_percent","now_cost",
                           "element_type","team_code"]

    df.drop(columns=[col for col in df if col not in final_table_columns], inplace=True)
    #create a column to specify what season the data is for
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
    gcp_cloud_storage_bucket_block = GcsBucket.load("fpl-gcs")
    gcp_cloud_storage_bucket_block.upload_from_path(from_path=path, to_path=path, timeout=(10,200))
    return



@flow()
def testing(yearOne: int, yearTwo: int):
    dataset_url = f"https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/20{yearOne}-{yearTwo}/players_raw.csv"
    dataName = "raw_players"

    df = fetchData(dataset_url)
    clean = cleanData(df, yearOne, yearTwo)
    write_local(clean, yearOne, yearTwo, dataName)
    # write_gcs(path)

@flow() #loop through all possible years of data
def etl_parent_flow(yr:list[int], yrs:list[int]):
    for y, x in zip(yr,yrs):
        testing(y,x)




if __name__ == "__main__":
    yr = [16,17,18,19,20,21,22]
    yrs = [17,18,19,20,21,22,23]
    etl_parent_flow(yr,yrs)
