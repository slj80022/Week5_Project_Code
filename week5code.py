##input directory C:\Users\sally\School\Week5>##
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
ax.get_yaxis().set_major_formatter(
    matplotlib.ticker.FuncFormatter(lambda y, p: format(int(y), ',')))
ax.grid(False)
plt.tight_layout()
plt.savefig('crimelineplot2.png')


##create a stacked area chart Graph 2##
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

###Graph 3
df3 = pd.read_csv('crime2.csv')
crime3= pd.DataFrame(df3)
del crime3['CrimesIndex']
print(crime3)
columns = list(crime3.columns)
import matplotlib.patches as mpatches
from textwrap import wrap
Thefts = crime3.iloc[:,7]
Burglaries = crime3.iloc[:,6]
Auto_Thefts = crime3.iloc[:,8]
plt.figure(figsize=(10,7))
graphTheft = plt.bar(x=crime3.Year, height = crime3.Thefts, width=0.35)
graphBurglaries = plt.bar(x=crime3.Year, height = crime3.Burglaries, width = 0.35, bottom = crime3.Burglaries)
graphAuto_Thefts = plt.bar(x=crime3.Year, height = crime3.Auto_thefts, width = 0.35, bottom = crime3.Auto_thefts+crime3.Burglaries)
plt.xlabel('Year')
plt.ylabel('Number of Crimes Committed')
plt.title('Top 3 Crimes in Denver (2001-2013)')
plt.legend(loc=1, fontsize = 'medium')
plt.savefig('crimeBarplot.png')

##I can't figure out why the legend isn't showing up on the graph but the code isn't producing any errors.
