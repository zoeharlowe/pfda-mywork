# knock_weather.py
# Lab on a CSV file about recorded weather in Knock Airport
# Author: Zoe McNamara Harlowe

import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

# Read in dataset
filename = "knock_weather2.csv"
df = pd.read_csv(filename, skiprows = 19)

# Is there a correlation between mean temp and month?
corrtemp = df["month"].corr(df["meant"])
#print(corrtemp)   Printed out as 0.26 - weak correlation

# Create new dataframe
cleandf = df[["month", "wdsp"]]

# Got an error - https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
pd.options.mode.copy_on_write = True

# Drop null values from new df
cleandf['wdsp'] = cleandf.loc[:,('wdsp')].replace(' ', np.nan)
cleandf.dropna(inplace = True)

# Cast wdsp values to floats
cleandf['wdsp'] = cleandf['wdsp'].astype(float)

# Now to find correlation
corrwind = cleandf["month"].corr(cleandf["wdsp"])
# print(corrwind)  -0.2.. a weak negative correlation

# Regression
sns.set_style("whitegrid")
sns.lmplot(x='month', y='wdsp', order = 3, data = cleandf)
plt.savefig("lmplot_knock_weather.png")