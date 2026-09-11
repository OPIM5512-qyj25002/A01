from sklearn.datasets import fetch_california_housing
import os
import pandas as pd
import matplotlib.pyplot as plt

# Load California Housing dataset
housing = fetch_california_housing(as_frame=True)

# Features + target as a single DataFrame
df = housing.frame

# Quick check
print(df.head())
print(df.shape)


#creating box plots
os.makedirs('figs', exist_ok=True)

# Boxplot 1: Median Income
plt.figure(figsize=(5, 5))
df.boxplot(column='MedInc')
plt.title('Median Income')
plt.savefig('figs/boxplot_medinc.png', dpi=150, bbox_inches='tight')
plt.show()

# Boxplot 2: House Age
plt.figure(figsize=(5, 5))
df.boxplot(column='HouseAge')
plt.title('House Age')
plt.savefig('figs/boxplot_houseage.png', dpi=150, bbox_inches='tight')
plt.show()

# Boxplot 3: Median House Value
plt.figure(figsize=(5, 5))
df.boxplot(column='MedHouseVal')
plt.title('Median House Value')
plt.savefig('figs/boxplot_medhouseval.png', dpi=150, bbox_inches='tight')
plt.show()
