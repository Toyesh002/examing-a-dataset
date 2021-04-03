# import numpy as np
# import csv
import pandas as pd
# from matplotlib import pyplot as plt
# import tensorflow as tf

df= pd.read_csv(filepath_or_buffer="D:/TF/california_housing_train.csv")
df['median_house_value']/=1000.0
print(df.head())
print(df.describe())

