# tips.py
# Lab on built-in Seaborn 'tips' dataset 
# Author: Zoe McNamara Harlowe

import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

# Load dataset
df = sns.load_dataset('tips')
print(df.head(5))

# Regression analysis
sns.set_style('whitegrid')
sns.lmplot(x='size', y='tip', data=df, x_estimator=np.mean)

plt.show()

