!pip install opendatasets
!pip install kagglehub

import kagglehub
import opendatasets as od
import os
import pandas as pd

import sqlite3


#Kaggle dataset download path
file_path = kagglehub.dataset_download("mjshri23/life-expectancy-and-socio-economic-world-bank")

#Life expectancy at birth dataset
expactancy_birth="https://databank.worldbank.org/reports.aspx?source=2&series=SP.DYN.LE00.IN&country=csv"

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


life_exp_csv = os.path.join(data_directory, r"E:\DS Semester Study\Winter 2024-25\MADE\life expectancy.csv")
output_db = os.path.join(data_directory, f"E:\DS Semester Study\Winter 2024-25\MADE\life expectancy.db")


birth_exp_csv = os.path.join(data_directory, r"E:\DS Semester Study\Winter 2024-25\MADE\birth expectancy.csv")
birth_output_db = os.path.join(data_directory, r"E:\DS Semester Study\Winter 2024-25\MADE\birth expectancy.db")

# Function to clean and reshape life expectancy and socio-economic data
def clean_and_filter_data(file_path, american_countries):
    # Read the dataset
    df = pd.read_csv(file_path)
    
   
    df_filtered = df[df["Country Name"].isin(american_countries)]
    
    columns_to_keep = [
        "Country Name", "Country Code", "Year", "Life Expectancy World Bank", "IncomeGroup",
        "Health Expenditure %", "Education Expenditure %", "CO2","Prevelance of Undernourishment","Region","Sanitation","Unemployment"
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
    cleaned_csv_path = os.path.join(data_directory, r"E:\DS Semester Study\Winter 2024-25\MADE\life_expectancy_cleaned.csv")
    cleaned_data.to_csv(cleaned_csv_path, index=False)
    print(f"Cleaned data saved as CSV at {cleaned_csv_path}.")
    export_to_sqlite(cleaned_data, r"E:\DS Semester Study\Winter 2024-25\MADE\life_expectancy_data", output_db)
else:
    print(f"Dataset not found at {life_exp_csv}. File is downloaded and placed correctly.")
    

    
#------ Life expectancy birth Data-------------

#expactancy_birth = "https://api.worldbank.org/v2/en/indicator/SP.DYN.LE00.IN?downloadformat=csv"
output_dir = "../data"
os.makedirs(output_dir, exist_ok=True)
    
    # Function to clean and reshape brith expectancy
def clean_and_filter_data(expactancy_birth, american_countries):
    # Read the dataset
    df = pd.read_csv(expactancy_birth)
    
   
    df_filtered = df[df["Country Name"].isin(american_countries)]
    
    columns_to_keep = [
        "Country Name", "Country Code", "1990", "2000", "2014",
        "2015","2016","2017","2018","2019","2020",
        "2021","2022"
        
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
if os.path.exists(birth_exp_csv):
    print("Processing Birth Expectancy data...")
    cleaned_data = clean_and_filter_data(birth_exp_csv, american_countries)
    cleaned_csv_path = os.path.join(data_directory, r"E:\DS Semester Study\Winter 2024-25\MADE\birth_expectancy_cleaned.csv")
    cleaned_data.to_csv(cleaned_csv_path, index=False)
    print(f"Cleaned data saved as CSV at {cleaned_csv_path2}.")
    export_to_sqlite(cleaned_data, r"E:\DS Semester Study\Winter 2024-25\MADE\birth_expectancy_data", birth_output_db)
else:
    print(f"Dataset not found at {birth_exp_csv}. File is downloaded and placed correctly.")
