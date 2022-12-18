#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])
string_data


# In[2]:


string_data.isnull()


# In[3]:


from numpy import nan as NA
data = pd.Series([1, NA, 3.5, NA, 7])
data.dropna()


# In[6]:


data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA],
                     [NA, NA, NA], [NA, 6.5, 3.]])
cleaned = data.dropna()
data


# In[7]:


print(cleaned)


# In[8]:


df = pd.DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] = NA
df


# In[9]:


#Filling In Missing Data
df.fillna(0)


# In[10]:


df.fillna({1: 0.5, 2: 0})


# In[11]:


#Removing Duplicates
data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                     'k2': [1, 1, 2, 3, 3, 4, 4]})
data


# In[12]:


data.duplicated()


# In[13]:


data.drop_duplicates()


# In[14]:


# Transforming Data
data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
                              'Pastrami', 'corned beef', 'Bacon',
                              'pastrami', 'honey ham', 'nova lox'],
                     'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
data


# In[15]:


meat_to_animal = {
 'bacon': 'pig',
 'pulled pork': 'pig',
 'pastrami': 'cow',
 'corned beef': 'cow',
 'honey ham': 'pig',
 'nova lox': 'salmon'
}


# In[16]:


lowercased = data['food'].str.lower()
lowercased


# In[17]:


data['animal'] = lowercased.map(meat_to_animal)
data


# In[ ]:




