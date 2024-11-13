!pip install opendatasets

import opendatasets as od
import os
import pandas as pd

#Kaggle dataset download path

dataset = 'https://www.kaggle.com/datasets/mjshri23/life-expectancy-and-socio-economic-world-bank?select=life+expectancy.csv'
od.download(dataset)


data_dir = '.\life-expectancy-and-socio-economic-world-bank'
os.listdir(data_dir)

#  Here ['life expectancy.csv']
life_df = pd.read_csv('Life expectancy.csv')
life_df
