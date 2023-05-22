#!/usr/bin/env python
# coding: utf-8

# # Python Basics

# In[90]:


list5=[1,4,3,2,1,2,4,6,4]


# In[3]:


list5.count(2)


# In[4]:


get_ipython().run_line_magic('pinfo', 'list5.index')


# In[6]:


list5.index(4)


# In[94]:


list5.index(4,5) # it gives the index of first occuring and here we consider the number comes on second time oer second place


# In[9]:


list4=[2,4,10,2,12,4,19,3,31,12,45,67,12]


# In[10]:


list4.index(12,5)   # give me the index of 12 when it occurs after 5th position


# In[11]:


list4.reverse()


# In[12]:


list4


# In[19]:


list4.sort() #by default accending order


# In[14]:


list4


# In[17]:


list4.sort(reverse=True)


# In[18]:


list4


# In[20]:


#Explicit-- add in list randomly
# Implicit--list4[2]=100  ## Means Mutable


# In[21]:


# string and number are immutable
# Lists are Mutable


# In[22]:


list4[2]


# In[23]:


list4


# In[25]:


list4[2]=100
list4


# # Data Type ---- SET

# #### A well defined collection of unique elements 
# #### Unordered
# ### Immutable
# #### It is denoted by {}
# #### Duplicay is not allowed

# In[28]:


u={0,1,2,3,4,5,6,7,8,9}
a={2,3,4,5}
b={2,4,6,8}
c={4,6,10,2,4,1,4,10,4,100}


# In[29]:


d={4,6,10,2,4,1,4,10,100}


# In[32]:


d   # remove duplicates because this's a set


# In[33]:


a.intersection(b)  # It give's the common values from both sets


# This is just like Inner Join


# In[35]:


a.union(b)  # records from both sets but it does'nt keep duplicated records


# In[36]:


a.difference(b)   # A-B (Records of A which are not in B) Salary - Credit


# In[38]:


b.difference(a)


# In[40]:


a


# In[41]:


b


# In[43]:


a.symmetric_difference(b) # (A union B)--(A int B) # all record have common

# like we identify those who have not any bank account or credit card


# In[45]:


a.isdisjoint(b) # two sets are said to be disjoint,if there is no common element 


# In[46]:


b


# In[47]:


c


# In[48]:


b.isdisjoint(c)


# In[49]:


b.issubset(a)


# In[50]:


b.issubset(u)


# In[53]:


a.discard(2)  # it remove the elements from the set ,If the element is the member then delete else does nothing
a


# In[54]:


a


# In[55]:


b


# In[56]:


a.intersection_update(b)   # this function is just like when we 


# In[57]:


a


# In[58]:


b


# # Index & Slicing

# In[59]:


u


# In[60]:


d


# In[61]:


d[1]


# ## Data type -- Tuple
# * It has all the properties of list except it is a immutable
# * It is denoted by ()
# * It is ordered form

# In[64]:


x=3,4,5,10,3,4,3,3


# In[65]:


x


# In[66]:


y=(10,10,2,34,10,3,2,2,12)


# In[67]:


y


# In[68]:


x[2]


# In[69]:


x[2]=10


#  ## Data Type = Dictionary
#  * It is base on key value pair concept
#  * It is ordered
#  * It is mutuable
#  * It is denoted by {}

# In[78]:


d1={'countries':['India','Canada','Australia'],'Income':100,'Language':'English','Names':{'A','B','F','D','A','C'}}


# In[79]:


d1


# In[80]:


# Index & slicing


# In[81]:


d1['countries'] # Here Key is the Index


# In[82]:


d1['Income']


# In[83]:


d1['countries'][1]  # Only pick up the canada country


# In[85]:


d1.keys()


# In[86]:


d1.values()


# In[87]:


d1.items()


# In[88]:


d1['Income']=800000


# In[89]:


d1


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




