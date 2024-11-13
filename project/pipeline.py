!pip install opendatasets

import kaggle
import zipfile
import os
import opendatasets as od



dataset = 'https://www.kaggle.com/datasets/mjshri23/life-expectancy-and-socio-economic-world-bank?select=life+expectancy.csv'
od.download(dataset)



# Define Kaggle dataset and download path
dataset = "mjshri23/life-expectancy-and-socio-economic-world-bank"
download_path = "data"

# Download dataset using Kaggle API
kaggle.api.dataset_download_files(dataset, path=download_path, unzip=True)

# Verify download by listing files
print("Files downloaded to 'data' directory:")
print(os.listdir(download_path))

import pandas as pd
file_path = os.path.join(download_path, "life-expectancy-data.csv")  # Adjust filename as needed
df = pd.read_csv(file_path)
print(df.head())
