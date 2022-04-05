import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


df = pd.read_csv('chamber.csv')
df.head()

ordered_df = df.sort_values(by='Map')
my_range=range(1,len(df.index)+1)

plt.hlines(y=my_range, xmin=ordered_df['NA'], xmax=ordered_df['EMEA'], color='grey', alpha=0.4)
plt.scatter(ordered_df['NA'], my_range, color='red', alpha=1, label='NA')
plt.scatter(ordered_df['EMEA'], my_range, color='blue', alpha=0.8 , label='EMEA')
plt.legend()

# Add title and axis names
plt.yticks(my_range, ordered_df['Map'])
plt.title("Chamber Pick Rates NA and EMEA", loc='left')
plt.xlabel('Pick Percentage')
plt.ylabel('Maps')
figure(figsize=(10, 10), dpi=80)
plt.savefig('mlot.png')
