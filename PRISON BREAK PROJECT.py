#!/usr/bin/env python
# coding: utf-8

# # Analyzing Data

# ## Prison Helicopter Escapes

# We begin by importing some helper functions.

# In[1]:


from helper import *


# ## Get the Data

# Now, let's get the data from the [List of helicopter prison escapes](https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes) Wikipedia article.

# In[4]:


url = "https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes"
data = data_from_url(url)


# In[7]:


for row in data[:3]:
    print(row)


# In[8]:


index = 0
for row in data:
    data[index] = row[:-1]
    index += 1


# In[9]:


print(data[:3])


# 
# ## Extracting the Year
# 
# In the code cell below, we iterate over data using the iterable variable row and: * With every occurrence of row[0], we refer to the first entry of row, i.e., the date. * Thus, with date = fetch_year(row[0]), we're extracting the year out of the date in row[0] and assiging it to the variable date. * We then replace the value of row[0] with the year that we just extracted.
# 

# In[10]:


for row in data:
    date = fetch_year(row[0])
    row[0] = date


# In[11]:


print(data[:3])


# ## Attempts per Year

# In[12]:


min_year = min(data, key=lambda x: x[0])[0]
max_year = max(data, key=lambda x: x[0])[0]


# In[13]:


print(min_year)
print(max_year)


# In[14]:


years = []
for year in range(min_year, max_year + 1):
    years.append(year)


# In[15]:


print(years)


# In[16]:


attempts_per_year = []
for year in years:
    attempts_per_year.append([year, 0])


# In[17]:


for row in data:
    for year_attempt in attempts_per_year:
        year = year_attempt[0]
        if row[0] == year:
            year_attempt[1] += 1
            
print(attempts_per_year)


# In[18]:


get_ipython().run_line_magic('matplotlib', 'inline')
barplot(attempts_per_year)


# In[19]:


countries_frequency = df["Country"].value_counts()


# In[21]:


print_pretty_table(countries_frequency)


# In[ ]:




