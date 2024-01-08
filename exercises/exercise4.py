import zipfile
import urllib.request
import pandas as pd
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.types import *

# Step 1: Download and unzip data
download_url = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"
zip_file_path = "mowesta-dataset.zip"
extracted_folder_path = "mowesta-dataset"

urllib.request.urlretrieve(download_url, zip_file_path)

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder_path)

# Step 2: Reshape data
csv_file_path = f"{extracted_folder_path}/data.csv"
df = pd.read_csv(csv_file_path, sep=';', decimal=',', on_bad_lines='skip')

columns_to_keep = ["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"]
df = df[columns_to_keep]

# Rename columns
df.rename(columns={"Temperatur in °C (DWD)": "Temperatur", "Batterietemperatur in °C": "Batterietemperatur"}, inplace=True)

# Discard columns to the right of "Geraet aktiv"
df = df.iloc[:, :df.columns.get_loc("Geraet aktiv") + 1]

# Step 3: Transform data
df["Temperatur"] = (df["Temperatur"] * 9/5) + 32
df["Batterietemperatur"] = (df["Batterietemperatur"] * 9/5) + 32

# Step 4: Validate data
# For simplicity, we'll assume "Geraet" should be an id over 0
df = df[df["Geraet"] > 0]


# Step 5: Use fitting SQLite types and write data into SQLite database
engine = create_engine('sqlite:///temperatures.sqlite')
df.to_sql('trainstops', engine, index=False, if_exists='replace', dtype={
    "Geraet": BigInteger,
    "Hersteller": Text,
    "Model": Text,
    "Monat": Text,
    "Temperatur": Float,
    "Batterietemperatur": Float,
    "Geraet aktiv": BigInteger
})

print("Data pipeline successfully executed.")