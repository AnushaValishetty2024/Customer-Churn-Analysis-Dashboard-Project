import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

print(os.listdir())

sns.set_style("whitegrid")

df = pd.read_csv("Customer_Data.csv")

print("Dataset loaded successfully!")

print(df.head())

print("\nShape of Dataset:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe()) 
print("\nMissing Values:")
print(df.isnull().sum())
plt.figure(figsize=(6,4))

sns.countplot(x='Customer_Status', data=df)

plt.title("Customer Churn Distribution")
plt.show()
plt.figure(figsize=(6,4))

sns.countplot(x='Customer_Status', data=df)

plt.title("Customer Churn Distribution")
plt.show()