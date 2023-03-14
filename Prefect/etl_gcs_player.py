from pathlib import Path
import pandas as pd



def fetchData(dataset_url: str):
    df = pd.read_csv(dataset_url)
    return df

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


def write_local(df: pd.DataFrame, yearOne: int, yearTwo: int, dataName: str):
    Path(f"player_data").mkdir(parents=True, exist_ok=True)
    path = Path(f"player_data/{dataName}_20{yearOne}-{yearTwo}.parquet")
    df.to_parquet(path)
    print(path)


def testing():
    yearOne = 16
    yearTwo = 17
    dataset_url = f"https://github.com/vaastav/Fantasy-Premier-League/raw/master/data/20{yearOne}-{yearTwo}/players_raw.csv"
    dataName = "raw_players"

    df = fetchData(dataset_url)
    clean = cleanData(df, yearOne, yearTwo)
    write_local(clean, yearOne, yearTwo, dataName)

if __name__ == "__main__":
    testing()
