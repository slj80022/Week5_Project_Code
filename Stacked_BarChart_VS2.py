import os
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
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
df.plot(kind='bar', stacked=True, colormap=cmap1)


plt.savefig('crimeBarplot.png')
