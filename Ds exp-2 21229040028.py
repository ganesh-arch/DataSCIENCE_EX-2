#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd


# In[34]:


df=pd.read_csv("weight.csv")
df


# In[35]:


df.drop("Gender",axis=1,inplace=True)


# In[39]:


df


# In[38]:


df.boxplot()


# In[40]:


from scipy import stats


# In[41]:


import numpy as np


# In[44]:


z=np.abs(stats.zscore(df)) 


# In[45]:


z


# In[46]:


df1=df.copy()


# In[47]:


df1=df1[(z<3).all(axis=1)]


# In[48]:


df2=df.copy()


# In[49]:


q1=df2.quantile(0.25)


# In[50]:


q3=df2.quantile(0.75)


# In[51]:


IQR=q3-q1


# In[53]:


df2_new=df2[((df2>=q1-1.5*IQR)&(df2<=q3+1.5*IQR)).all(axis=1)]
df2_new

