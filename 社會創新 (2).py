#!/usr/bin/env python
# coding: utf-8

# ### 社會創新組織
# ### https://si.taiwan.gov.tw/Home/News?fid=144

# In[1]:


# 使用request套件獲得網頁資訊
# 使用BeautifulSoup解析網頁內容
import requests
from bs4 import BeautifulSoup


# In[2]:


# 出現SSLError: HTTPSConnectionPool錯誤解決方式，加上verify=False
result = requests.get("https://si.taiwan.gov.tw/Home/News?fid=144",verify=False) #get 該網址的 HTML
#print(result.text) #print 結果至畫面
b = BeautifulSoup(result.text, 'html.parser') #將網頁資料以 html.parser 解析器來解析
#print(b)


# In[12]:


# 可以發現 href不是完整的網址，所以要把前面的網址補上
headers = 'https://si.taiwan.gov.tw/Files/News/144/'
#b.find(class_="container file_item_container")
link = headers + str(b.find(class_="file_item").text).strip()
print(link)


# In[6]:


alink = b.select('.container file_item_container')
print(alink)


# In[28]:


sys.getdefaultencoding()


# In[13]:


import pandas as pd
newspd = pd.read_excel(link, encoding = "ansi")
newspd.head()


# In[15]:


from encodings.aliases import aliases
for encoding in set(aliases.values()):
    try:
        pd.read_excel(link, encoding=encoding)
    except:
        continue
    print('Acceptable coding: ' + encoding)


# In[23]:


from encodings.aliases import aliases
for encoding in set(aliases.values()):
    try:
        newspd = pd.read_excel(link, encoding=encoding)
        print(encoding)
        newspd.head()
    except:
        continue
    print('Acceptable coding: ' + encoding)


# In[ ]:




