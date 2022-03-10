import pandas as pd
import matplotlib.pyplot as plt
import mplsoccer
import highlight_text
from mplsoccer import Bumpy
import numpy as np

df = pd.read_csv('pltable.csv')
df.head()

df = df.T




df.columns = df.iloc[0]
df = df.iloc[1:]

df.head()


week = ["Week " + str(num) for num in range(1, 29)]



highlight_dict = {
    "Arsenal": "red",
    "Chelsea": "blue",
    "Manchester United": "gold"
}

# instantiate object
bumpy = Bumpy(
    scatter_color="#282A2C", line_color="#252525",
    rotate_xticks=90,
    ticklabel_size=15,
    scatter_primary='D',
    show_right=True,
    plot_labels=True,
    alignment_yvalue=0.1,
    alignment_xvalue=0.065
)

# plot bumpy chart
fig, ax = bumpy.plot(
    x_list=week,
    y_list=np.linspace(1, 20, 20).astype(int),
    values=df,
    secondary_alpha=0.5,
    highlight_dict=highlight_dict,
    figsize=(18, 18),  #
    y_label='Position',  # label name
    ylim=(-0.1, 23),
    lw=2.5,
)

fig.text(s = 'Premier League Through Week 28',x = .5, y = .85,
         c = 'white',size=24,weight='bold',ha='center'
        )

highlight_text.fig_text(x=.5, y= .84,
                       s = 'Comparing <Arsenal> & <Chelsea>',
                       highlight_textprops = [
                           {"color":'red'},
                           {"color":'blue'},
                       ],
                        fontsize = 20,
                        color = 'white',
                        ha='center'
                       )

plt.savefig('doo.png')
#plt.savefig('doo.pdf')
