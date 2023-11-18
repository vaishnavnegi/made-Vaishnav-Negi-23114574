import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import *

# Download and read the CSV data
url = "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"
df = pd.read_csv(url, sep=';')

# Drop the "Status" column
df = df.drop(columns=['Status'])

# Convert 'Laenge' and 'Breite' to numeric types
df['Laenge'] = df['Laenge'].str.replace(',', '.').astype(float)
df['Breite'] = df['Breite'].str.replace(',', '.').astype(float)

#Applying the specified filters
df = df[df['Verkehr'].isin(['FV', 'RV', 'nur DPN'])]
df = df[(df['Laenge'] >= -90) & (df['Laenge'] <= 90)]
df = df[(df['Breite'] >= -90) & (df['Breite'] <= 90)]
df = df[df['IFOPT'].str.match('^[A-Za-z]{2}:\d+:\d+(?::\d+)?$', na=False)]
df = df.dropna()

# Create SQLite database and write the cleaned data
engine = create_engine('sqlite:///trainstops.sqlite')
df.to_sql('trainstops', engine, index=False, if_exists='replace', dtype={
    "BFNr": BigInteger,
    "Station": Text,
    "Category": Text,
    "Verkehr": Text,
    "Laenge": Float,
    "Breite": Float,
    "Land": Text,
    "Betreiber": Text,
    "PLZ": Text,
    "Ort": Text,
    "IFOPT": Text
})