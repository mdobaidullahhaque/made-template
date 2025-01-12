!pip install opendatasets

import opendatasets as od
import os
import pandas as pd

import sqlite3

#Kaggle dataset download path
dataset = 'https://www.kaggle.com/datasets/mjshri23/life-expectancy-and-socio-economic-world-bank?select=life+expectancy.csv'
od.download(dataset)

data_dir = '.\life-expectancy-and-socio-economic-world-bank'
os.listdir(data_dir)

# Define directories
data_directory = "../data"
if not os.path.exists(data_directory):
    os.makedirs(data_directory)

# North and South American countries list
american_countries = [
    "Canada", "United States", "Mexico", "Bermuda", "Bahamas, The",
    "Barbados", "Cuba", "Haiti", "Dominican Republic", "Jamaica",
    "Trinidad and Tobago", "Saint Kitts and Nevis", "Antigua and Barbuda",
    "Saint Lucia", "Saint Vincent and the Grenadines", "Grenada", "Belize",
    "Panama", "Costa Rica", "El Salvador", "Honduras", "Nicaragua",
    "Guatemala", "Argentina", "Brazil", "Chile", "Colombia", "Peru",
    "Venezuela, RB", "Ecuador", "Bolivia", "Uruguay", "Paraguay", "Guyana",
    "Suriname", "French Guiana"
]

life_exp_csv = os.path.join(data_directory, "LifeExpectancyData.csv")
output_db = os.path.join(data_directory, "life_socio_economic_data.db")

# Function to clean and reshape life expectancy and socio-economic data
def clean_and_filter_data(file_path, countries):
    # Read the dataset
    df = pd.read_csv(file_path)
   
    df_filtered = df[df["Country Name"].isin(countries)]
    # Select relevant columns (e.g., life expectancy, GDP per capita, etc.)
    columns_to_keep = [
        "Country Name", "Country Code", "Year", "Life Expectancy", "GDP per capita",
        "Health expenditure (% of GDP)", "Education expenditure (% of GDP)"
    ]
    df_cleaned = df_filtered[columns_to_keep]
    # Drop rows with missing values
    df_cleaned = df_cleaned.dropna()
    return df_cleaned

# Save cleaned data to SQLite
def export_to_sqlite(df, table_name, db_path):
    with sqlite3.connect(db_path) as conn:
        df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"Saved table '{table_name}' to SQLite database at {db_path}.")

# Clean and save the dataset
if os.path.exists(life_exp_csv):
    print("Processing Life Expectancy and Socio-Economic data...")
    cleaned_data = clean_and_filter_data(life_exp_csv, american_countries)
    cleaned_csv_path = os.path.join(data_directory, "life_socio_economic_cleaned.csv")
    cleaned_data.to_csv(cleaned_csv_path, index=False)
    print(f"Cleaned data saved as CSV at {cleaned_csv_path}.")
    export_to_sqlite(cleaned_data, "life_socio_economic_data", output_db)
else:
    print(f"Dataset not found at {life_exp_csv}. Please ensure the file is downloaded and placed correctly.")

#  Here ['life expectancy.csv']
#life_df = pd.read_csv('Life expectancy.csv')
#life_df
