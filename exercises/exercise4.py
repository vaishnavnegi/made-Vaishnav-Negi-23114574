import zipfile
import urllib.request
import random
import string
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import *

# Step 1: Download and unzip data
download_url = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"
zip_file_path = "mowesta-dataset.zip"
extracted_folder_path = "mowesta-dataset"

urllib.request.urlretrieve(download_url, zip_file_path)

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder_path)

# Existing column names
existing_columns = ["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)",
                    "Latitude (WGS84)", "Longitude (WGS84)", "Verschleierung (m)",
                    "Aufenthaltsdauer im Freien (ms)", "Batterietemperatur in °C", "Geraet aktiv"]

# Number of additional random columns needed to reach a total of 452 columns
additional_columns_needed = 453 - len(existing_columns) #453 is the number of total columns, obtained by opening the file in excel

# Generate random column names
random_columns = [''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) for _ in range(additional_columns_needed)]

# Combine existing and random column names
all_columns = existing_columns + random_columns

# Convert the list to a ';' separated string
columns_string = ';'.join(all_columns)

# Step 2: Reshape data
csv_file_path = f"{extracted_folder_path}/data.csv"
df = pd.read_csv(csv_file_path,header=None, names=all_columns, skiprows=1, sep=';', decimal=',')

columns_to_keep = ["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"]
df = df[columns_to_keep]

# Rename columns
df.rename(columns={"Temperatur in °C (DWD)": "Temperatur", "Batterietemperatur in °C": "Batterietemperatur"}, inplace=True)

# Discard columns to the right of "Geraet aktiv"
df = df.iloc[:, :df.columns.get_loc("Geraet aktiv") + 1]

# Handle empty values
df.dropna(inplace=True)

# Step 3: Transform data
df["Temperatur"] = (df["Temperatur"] * 9/5) + 32
df["Batterietemperatur"] = (df["Batterietemperatur"] * 9/5) + 32

# Step 4: Validate data
# For simplicity, we'll assume "Geraet" should be an id over 0
df = df[df["Geraet"] > 0]


# Step 5: Use fitting SQLite types and write data into SQLite database
engine = create_engine('sqlite:///temperatures.sqlite')
df.to_sql('temperatures', engine, index=False, if_exists='replace', dtype={
    "Geraet": BigInteger,
    "Hersteller": Text,
    "Model": Text,
    "Monat": BigInteger,
    "Temperatur": Float,
    "Batterietemperatur": Float,
    "Geraet aktiv": Text
})

print("Data pipeline successfully executed.")
