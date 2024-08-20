#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import json


# In[2]:


json.__version__


# In[3]:


with open("Desktop/t20 circlet analysis/t20_json_files/t20_wc_match_results.json") as f:
    data= json.load(f)
dataframe = pd.DataFrame(data[0] ['matchSummary'])
dataframe.head()


# In[12]:


dataframe.shape


# In[4]:


dataframe.rename({'scorecard' : 'match_id'}, axis = 1, inplace = True)
dataframe.head()


# In[20]:


match_ids_dict = {}

for index,row in dataframe.iterrows():
    key1 = row['team1'] + " Vs " + row['team2']
    key2 = row['team2'] + " Vs " + row['team1']
    
    
    match_ids_dict[key1] = row['match_id']
    match_ids_dict[key2] = row['match_id']

match_ids_dict     
        


# In[ ]:





# 

# In[7]:


match_ids_df = pd.DataFrame(list(match_ids_dict.items()), columns=['match', 'match_id'])
match_ids_df


# #batting data#
# 

# In[8]:


with open("Desktop/t20 circlet analysis/t20_json_files/t20_wc_batting_summary.json") as f:
    data1= json.load(f)

all_records = []

for rec in data1:
    all_records.extend(rec['battingSummary'])
batting_data=pd.DataFrame(all_records)
batting_data.tail()


# In[16]:


batting_data['out/not out']= batting_data.dismissal.apply(lambda x : "out" if len(x) > 0 else "not_out")
batting_data.head(20)


# In[9]:


batting_data.drop(columns=['dismissal'], inplace = True)
batting_data.head(20)


# In[10]:


batting_data["batsmanName"] = batting_data['batsmanName'].apply(lambda x : x.replace ('€',''))
batting_data["batsmanName"] = batting_data['batsmanName'].apply(lambda x : x.replace ('\xa0',''))


# In[11]:


batting_data['batsmanName'].head()


# In[21]:


batting_data["match_id"] = batting_data["match"].map(match_ids_dict)
batting_data.head()


# In[24]:


batting_data.to_csv('Desktop/t20 circlet analysis/t20_csv_files/fact_battting summary', index = False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




