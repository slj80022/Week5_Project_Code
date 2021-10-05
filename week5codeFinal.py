## Sally James ##
## Week 5 Project for MSDS 670  ##
## data from course -> content -> Course Datasets -> Easy -> Denver Crime 2001-2013'  ##

##input directory C:\Users\sally\School\Week5>##

##  create a line plot with multiple lines representing the crimes  ##
output_dir = r'C:\\Users\\sally\\School\\Week5'
import os
import matplotlib
import seaborn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
dpi = 300
os.getcwd()
df = pd.read_csv('Denver Crime 2001_2013.csv')
df1 = pd.read_csv('crime2.csv')
crime=pd.DataFrame(df1)
#remove crimes index since it's not a crime#
del crime['CrimesIndex']
print(crime)
columns = list(crime.columns)
#lineplot of Trends in Crime
ax=crime.plot.line(x="Year", y = "Murders")
plt.ylabel('Number of Murders')
ax.grid(False)
ax = crime.plot.line(x="Year")
ax.set_title('Denver Major Crimes 2001 - 2013', fontsize = 18)
plt.ylabel('Number of Crimes')
plt.xlabel('Year Crime Occurred')
plt.title('Denver Major Crimes 2001 - 2013')
ax.get_yaxis().set_major_formatter(
    matplotlib.ticker.FuncFormatter(lambda y, p: format(int(y), ',')))
ax.grid(False)
plt.tight_layout()
plt.savefig('crimelineplot2.png')


##  create a stacked area chart Graph 2  ##
df2 = pd.read_csv('crime2.csv')
crime2 = pd.DataFrame(df2)
del crime2['CrimesIndex']
print(crime2)
columns = list(crime2.columns)
plt.stackplot(crime2.Year,
[crime2['Murders'], crime2['Rapes'], crime2['Robberies'], crime2['Assaults'], crime2['Burglaries'], crime2['Thefts'], crime2['Auto_thefts'], crime2['Arson']],
labels = ['Murders', 'Rapes', 'Robberies', 'Assaults', 'Burglaries','Thefts', 'Auto_thefts', 'Arson'], 
alpha = 0.8)
plt.ylabel('Number of Crimes')
plt.legend(loc=1, fontsize='medium')
plt.savefig('crimeareaplot2.png')

##I couldn't get the code to work to add comma's into the y-axis labels even though the code ran without errors so I deleted the code.  I'm not sure what I did wrong.  I used the same code as above
##I also tried a couple of other methods.  None errored but none inserted the comma

###  Stacked bar chart redo with legend ##
import os
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap
matplotlib.style.use('ggplot')
output_dir = r'C:\\Users\\sally\\School\\Week5'
df3 = pd.read_csv('crime2.csv')
crime3= pd.DataFrame(df3)
del crime3['CrimesIndex']
print(crime3)
columns = list(crime3.columns)
import matplotlib.patches as mpatches
from textwrap import wrap
crimes = 'Murders', 'Rapes', 'Robberies', 'Assaults', 'Burglaries', 'Thefts', 'Auto_thefts', 'Arson'
colors = sns.color_palette("cubehelix", n_colors=len(crimes))
cmap1 = LinearSegmentedColormap.from_list("my_colormap", colors)
Thefts = crime3.iloc[:,6]
Burglaries = crime3.iloc[:,5]
Auto_Thefts = crime3.iloc[:,7]
Murders = crime3.iloc[:,1]
Rapes = crime3.iloc[:,2]
Robberies = crime3.iloc[:,3]
Assaults = crime3.iloc[:,4]
Arson = crime3.iloc[:,8]
plt.figure(figsize=(10,7))
graphTheft = plt.bar(x=crime3.Year, height = crime3.Thefts, width=0.35)
graphBurglaries = plt.bar(x=crime3.Year, height = crime3.Burglaries, width = 0.35, bottom = crime3.Burglaries)
graphAuto_Thefts = plt.bar(x=crime3.Year, height = crime3.Auto_thefts, width = 0.35, bottom = crime3.Auto_thefts+crime3.Burglaries)
graphMurders = plt.bar(x=crime3.Year, height = crime3.Murders, width = 0.35, bottom = crime3.Auto_thefts+crime3.Burglaries+crime3.Murders)
graphRapes = plt.bar(x = crime3.Year, height = crime3.Rapes, width = 0.35, bottom = crime3.Auto_thefts+crime3.Burglaries+crime3.Murders+crime3.Rapes)
graphRobberies = plt.bar(x=crime3.Year, height = crime3.Robberies, width = 0.35, bottom = crime3.Auto_thefts+crime3.Burglaries+crime3.Murders+crime3.Rapes+crime3.Robberies)
graphAssaults = plt.bar(x = crime3.Year, height = crime3.Assaults, width = 0.35, bottom = crime3.Auto_thefts+crime3.Burglaries+crime3.Murders+crime3.Rapes+crime3.Robberies+crime3.Assaults)
graphArson = plt.bar(x = crime3.Year, height = crime3.Arson, width = 0.35, bottom = crime3.Auto_thefts+crime3.Burglaries+crime3.Murders+crime3.Rapes+crime3.Robberies+crime3.Assaults+crime3.Arson)
crime3 = crime3.set_index('Year')
plt.xlabel('Year')
plt.ylabel('Number of Crimes Committed')
plt.title('Crimes in Denver (2001-2013)')
plt.legend(loc=1, fontsize = 'medium')
crime3.plot(kind='bar', stacked=True, colormap=cmap1)
plt.ylabel('Total Crimes Committed')
plt.title('Denver Major Crimes (2001-2013)')
plt.savefig('crimeBarplot2.png')

##I figured out how to do the stacked barchart with the legend but it keeps cutting off the labels of the axis even when I change the size.  This is the redo version
