import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

import highlight_text

df = pd.read_csv('TR.csv')

#set default colors
text_color = 'white'
background = '#313332'

df.head()

fig, ax = plt.subplots(figsize=(10,5))
fig.set_facecolor(background)
ax.patch.set_facecolor(background)

#set up our base layer
mpl.rcParams['xtick.color'] = text_color
mpl.rcParams['ytick.color'] = text_color

ax.grid(ls='dotted',lw=.5,color='lightgrey',axis='y',zorder=1)
spines = ['top','bottom','left','right']
for x in spines:
    if x in spines:
        ax.spines[x].set_visible(False)

sns.swarmplot(x='ACS',data=df,color='white',zorder=1)

plt.scatter(x=281.3,y=0,c='red',edgecolor='white',s=200,zorder=2)
plt.text(s='vakk',x=281.3,y=-.04,c=text_color)

plt.scatter(x=277.2,y=0,c='blue',edgecolor='white',s=200,zorder=2)
plt.text(s='H1ber',x=281.3,y=-.04,c=text_color)

plt.title('All VRLs Top ACS',c=text_color,fontsize=14)

plt.xlabel('ACS',c=text_color)
plt.savefig('doo.png')
