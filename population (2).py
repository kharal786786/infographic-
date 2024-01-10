#!/usr/bin/env python
# coding: utf-8

# # Import Libraries

# In[1]:


# Data Processing Libraries
#The project is about the visualization of population of the different countries in year 2022. four plots are drawn to show the visualization and dataset is taken from the kaggle.
import pandas as pd

# Data Visualization Libraries
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express  as px


# # Read Data

# In[2]:


df = pd.read_csv(r'C:\Users\HP\Desktop\worlds.csv')


# In[3]:


df.head()


# In[4]:


# !pip install plotly-geo==1.0.0
# !pip install geopandas==0.3.0
# !pip install pyshp==1.2.10
# !pip install shapely==1.6.3


# # Statistics of the Dataset

# In[5]:


print('There are ', df.shape[0], 'Countries Information in the Dataset and ', df.shape[1], 'columns representing different information about Country.' )


# In[6]:


df.describe()


# In[60]:


plt.figure(figsize = (45, 30))

plt.subplot(2, 2, 1)

sns.barplot(x = 'Country/Territory', y = '2022 Population', data=df.sort_values(['2022 Population']).iloc[:5, :])
plt.xticks()
plt.title('ID#22095431\nName#Abdullah Riaz\nThe project is about the population of the countries in the year 2022 and four plots are shown in the project\nThe plot shows Countries with Lowest Population and vetican city has the lowest population',size=25)

#plt.show()
plt.grid()


#plt.figure(figsize = (14, 8))
plt.subplot(2, 2, 2)
sns.barplot(x = 'Country/Territory', y = '2022 Population',
            data=df.sort_values(['2022 Population'], ascending=False).iloc[:5, :], )
plt.xticks()
plt.ticklabel_format(style='plain', axis='y')
plt.title('Countries with Highest Population and china has the highest population',size=25)
#plt.show()
plt.grid()
#plt.savefig(r'C:\Users\HP\Desktop\fi.png',dpi=(250),bbox_inches='tight')



plt.subplot(2, 2, 3)
list_pop = ['2022 Population', '2020 Population', '2015 Population',
       '2010 Population', '2000 Population', '1990 Population',
       '1980 Population', '1970 Population']
list_pop.reverse()
df_contient_pop = df.groupby(['Continent'])[list_pop].sum().reset_index()
df_contient_pop = df_contient_pop.melt(id_vars=["Continent"], 
        var_name="PopulationYear", 
        value_name="Population")
#plt.figure(figsize = (16, 8))
sns.lineplot(data=df_contient_pop, x="PopulationYear", y="Population", hue = 'Continent')
plt.xticks(rotation = 90)
plt.ticklabel_format(axis = 'y', style='plain')
plt.title('Population Growth over the Census and ASIA population has been increased over time \n', size = 25)
plt.grid()


plt.subplot(2, 2, 4)
populationwithincontinent = df.groupby(['Continent'])['2022 Population'].sum().reset_index(name = 'PopulationPerContinentsIn2020')
populationwithincontinent['PopulationInMillions'] =  (populationwithincontinent['PopulationPerContinentsIn2020'].astype(float)/1000000)
#plt.figure(figsize = (10, 7))
sns.barplot(x = 'Continent', y = 'PopulationInMillions', data=populationwithincontinent)
plt.xticks(rotation = 90)
plt.xlabel('Continent', size = 25)
plt.ylabel('Popultion in Millions', size = 25)
plt.title('Population in Continents and Asia has the highest population among all the continents \n', size = 25)
# plt.ticklabel_format(style='plain', axis='y')
plt.grid()

plt.savefig(r'C:\Users\HP\Desktop\fi.png',dpi=(400),bbox_inches='tight')


# In[ ]:




