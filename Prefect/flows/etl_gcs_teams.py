##created this so that i can load in team data to join to players data
## team data will change each year as teams get promoted/demoted - no structure to account for all teams from 16/17 season
from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket


@task(retries=3)
def fetchData(dataset_url: str):
    print(dataset_url)
    df = pd.read_csv(dataset_url)
    print(df.head())
    return df

@task()
def cleanData(df: pd.DataFrame):
    #creating a list of all columns that i want to keep in finalised dataset
    df.rename(columns={'name':'team'}, inplace=True)
    final_table_columns = ["id", "team"]
    df.drop(columns=[col for col in df if col not in final_table_columns], inplace=True)
    print(f"columns: {df.dtypes}")
    print(f"rows: {len(df)}")
    return df

@task() #create path if it doesnt exist and load all data into it
def write_local(df: pd.DataFrame, yearOne: int, yearTwo: int, dataName: str):
    Path(f"teams").mkdir(parents=True, exist_ok=True)
    path = Path(f"teams/{dataName}_20{yearOne}-{yearTwo}.parquet")
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



@flow()
def etl_flow(yearOne: int, yearTwo: int):
    dataset_url = f"https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/20{yearOne}-{yearTwo}/teams.csv"
    dataName = "teams"

    df = fetchData(dataset_url)
    clean = cleanData(df)
    path = write_local(clean, yearOne, yearTwo, dataName)
    write_gcs(path)

    
    # write_gcs(path)

@flow() #loop through all possible years of data
def etl_parent_flows(yr:list[int], yrs:list[int]):
    for y, x in zip(yr,yrs):
        etl_flow(y,x)


if __name__ == "__main__":
    yr = [19,20,21,22]
    yrs = [20,21,22,23]
    etl_parent_flows(yr,yrs)