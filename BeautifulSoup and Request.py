#!/usr/bin/env python
# coding: utf-8

# # BeautifulSoup and Requests

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


#specifiy where you are taking the html from
#assign the URL to a variable url

url = 'https://www.scrapethissite.com/pages/forms/'


# In[4]:


page = requests.get(url)


# In[6]:


#the page is what is sending that request and the dot text is retrieving the raw html

soup = BeautifulSoup(page.text, 'html')


# In[7]:


print(soup)


# In[9]:


#it has a hieracy while print(soup) does not have
print(soup.prettify())


# In[ ]:





# # FIND AND FIND_ALL

# In[10]:


soup.find('div')


# In[13]:


soup.find_all('div' , class_ = 'col-md-12')


# In[ ]:





# In[14]:


soup.find_all('p')


# In[15]:


soup.find_all('p', class_ = 'lead')


# In[16]:


# an error because we have used find_all instead of find. So use find to be able to change into text

soup.find_all('p', class_ = 'lead').text


# In[18]:


soup.find('p', class_ = 'lead').text


# In[19]:


#.strip()to clean the data a little bit

soup.find('p', class_ = 'lead').text.strip()


# In[20]:


soup.find_all('th')


# In[22]:


soup.find('th').text.strip()


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




