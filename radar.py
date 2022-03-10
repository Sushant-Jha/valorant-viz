import pandas as pd
import matplotlib.pyplot as plt
from soccerplots.radar_chart import Radar



#read in the data
df = pd.read_csv('TR.csv')
df.head()

df['Player'] = df['Player'].str.split('\n',expand=True)[0] #remove team names
df.head() 



df.Player.unique() #check if it actually worked



df = df[(df['Player']=='DeepMans') | (df['Player']=='JUGi')].reset_index()  #select the two [players]



df = df.drop(['index','Rnd','CL','D','Agents','Unnamed: 0','KAST','HS%','CL%'],axis=1) #drop the usleless colums 
df



#get parameters
params = list(df.columns) #creating a list of all the colums/metrics 
params = params[1:]
params



#add ranges to list of tuple pairs & fit percentile values for our stats for the players 
ranges = []
a_values = []
b_values = []

for x in params:
    a = min(df[params][x])
    a = a - (a*.25)
    
    b = max(df[params][x])
    b = b + (b*.25)
    
    ranges.append((a,b))
    
for x in range(len(df['Player'])):
    if df['Player'][x] == 'DeepMans':
        a_values = df.iloc[x].values.tolist()
    if df['Player'][x] == 'JUGi':
        b_values = df.iloc[x].values.tolist()
        
a_values = a_values[1:]
b_values = b_values[1:]

values = [a_values , b_values]
values 



#title 

title = dict(
    title_name='DeepMans',
    title_color = 'blue',
    subtitle_name = 'Wave',
    subtitle_color = 'blue',
    title_name_2='JUGi',
    title_color_2 = 'red',
    subtitle_name_2 = 'FOKUS',
    subtitle_color_2 = 'red',
    title_fontsize = 18,
    subtitle_fontsize=15
)



radar = Radar()

fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,
                         radar_color=['red','blue'],
                         alphas=[.75,.6],title=title,
                         compare=True)

plt.savefig('radar.png')
