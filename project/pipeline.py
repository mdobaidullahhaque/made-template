import os
import pandas as pd 
import sqlite3
import requests 

# dataset of life expectancy and socio economic
DATA_URL = "https://www.kaggle.com/datasets/mjshri23/life-expectancy-and-socio-economic-world-bank"

# Directories
DATA_DIR = "/data"
DB_FILE = os.path.join(DATA_DIR, "life_expectancy.db")

# Ensure the data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

def download_data(url, file_path):

    """This code download dataset from the given URL."""

    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f"Successfully downloaded data  and saved to {file_path}")
    else:
        print("Wrong!!\nFailed to download the dataset")


def main():
    # Download dataset (update with actual download handling if needed)
    csv_file_path = os.path.join(DATA_DIR, "life_expectancy.csv")
    download_data(DATA_URL, csv_file_path)
    
    # Here Load and clean data
    df = load_and_clean_data(csv_file_path)
    
    # Save cleaned data to SQLite
    save_to_sqlite(df, DB_FILE)

if __name__ == "__main__":
    main()


