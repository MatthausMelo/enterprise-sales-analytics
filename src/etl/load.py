from pathlib import Path
import pandas as pd
from etl.database import engine 

RAW_PATH = Path("data/raw")

def load_table(file_name: str, table_name: str):

    print(f"Loading {table_name}...")

    df = pd.read_csv(RAW_PATH / file_name)

    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False
    )

    print(f"{table_name} loaded ({len(df):,} rows)")