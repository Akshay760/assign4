#!/usr/bin/env python
# coding: utf-8

# # Q-2

# In[ ]:


from bs4 import BeautifulSoup
import requests


# In[24]:


page = requests.get('https://www.bcci.tv/international/fixtures')
page


# In[25]:


soup=BeautifulSoup(page.content)
soup


# In[37]:


match_title = soup.find('a',class_="match-tournament-name ng-binding")
match_title.text


# In[38]:


match_title


# In[39]:


series = soup.find('span',class_="ng-binding ng-scope")
series.text


# series

# In[40]:


place = soup.find('span',class_="ng-binding")
place.text


# In[18]:


place


# In[41]:


date = soup.find('div',class_="match-dates ng-binding")
date.text


# In[43]:


date


# In[42]:


time = soup.find('div',class_="match-time no-margin ng-binding")
time.text


# In[44]:


match_title = []
for i in soup.find_all ('a',class_="match-tournament-name ng-binding"):
    match_title.append(i.text)


# In[45]:


match_title


# In[46]:


place = []
for i in soup.find_all ('span',class_="ng-binding"):
    place.append(i.text)


# In[47]:


place


# In[48]:


date = []
for i in soup.find_all ('div',class_="match-dates ng-binding"):
    date.append(i.text)


# In[49]:


date


# In[50]:


time = []
for i in soup.find_all ('div',class_="match-time no-margin ng-binding"):
    date.append(i.text)


# In[51]:


time


# In[52]:


import pandas as pd
df=pd.DataFrame({'match_title':match_title,'place':place,'date':date,'time':time})
df


# # Q-1

# In[55]:


from bs4 import BeautifulSoup
import requests


# In[56]:


page = requests.get('https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos')
page


# In[57]:


soup=BeautifulSoup(page.content)
soup


# In[104]:


rank = soup.find('td',align="center")
rank


# In[136]:


rank.text


# In[ ]:


rank = soup.find('td',align="center")
rank


# In[138]:


rank.text


# In[137]:


name = soup.find('a',class_="mw-redirect",title="Baby Shark Dance")
name


# In[107]:


name.text


# In[108]:


artist = soup.find('a',href="/wiki/Pinkfong",title="Pinkfong")
artist


# In[109]:


artist.text


# In[110]:


uploading_date = soup.find('td',align="right")
uploading_date


# In[111]:


uploading_date.text


# In[121]:


rank=[]
for i in soup.find_all ('td',align="center"):
    rank.append(i.text)


# In[122]:


rank


# In[123]:


name=[]
for i in soup.find_all ('a',class_="mw-redirect",title="Baby Shark Dance"):
    name.append(i.text)


# In[124]:


name


# In[125]:


artist=[]
for i in soup.find_all ('a',href="/wiki/Pinkfong",title="Pinkfong"):
    artist.append(i.text)


# In[126]:


artist


# In[127]:


uploading_date=[]
for i in soup.find_all ('td',align="right"):
    uploading_date.append(i.text)


# In[128]:


uploading_date


# In[129]:


print(len(rank),len(name),len(artist),len(uploading_date))


# In[140]:


import pandas as pd
df=pd.DataFrame({'rank':rank,'name':name,'artist':artist,'uploading_date':uploading_date})
df
df.head(3)


# # q-7

# In[4]:


from bs4 import BeautifulSoup
import requests


# In[5]:


page=requests.get('https://www.imdb.com/list/ls095964455/')
page


# In[6]:


soup = BeautifulSoup(page.content)
soup


# In[7]:


name = soup.find('span',class_="lister-item-index unbold text-primary")
name


# In[8]:


name.text


# In[9]:


year_span = soup.find('span',class_="lister-item-year text-muted unbold")
year_span


# In[10]:


year_span.text


# In[11]:


genre = soup.find('span',class_="genre")
genre


# In[12]:


genre.text


# In[13]:


runtime = soup.find('span',class_="runtime")
runtime


# In[14]:


runtime.text


# In[15]:


rating = soup.find('div',class_="ipl-rating-star small")
rating


# In[16]:


rating.text


# In[17]:


vote = soup.find('span',class_="certificate")
vote


# In[18]:


vote.text


# In[19]:


name=[]
for i in soup.find_all ('span',class_="lister-item-index unbold text-primary"):
    name.append(i.text)


# In[20]:


name


# In[21]:


year_span=[]
for i in soup.find_all ('span',class_="lister-item-year text-muted unbold"):
    year_span.append(i.text)


# In[22]:


year_span


# In[23]:


genre=[]
for i in soup.find_all ('span',class_="genre"):
    genre.append(i.text)


# In[24]:


genre


# In[25]:


runtime=[]
for i in soup.find_all ('span',class_="runtime"):
    runtime.append(i.text)


# In[26]:


runtime


# In[27]:


rating=[]
for i in soup.find_all ('div',class_="ipl-rating-star small"):
    rating.append(i.text)


# In[28]:


rating


# In[29]:


vote=[]
for i in soup.find_all ('div',class_="wtw-option-standalone"):
    vote.append(i.text)


# In[30]:


vote


# In[31]:


print(len(name),len(year_span),len(genre),len(runtime),len(rating),len(vote))


# In[32]:



import pandas as pd
df=pd.DataFrame({'name':name,'year_span':year_span,'genre':genre,'runtime':runtime,'rating':rating,'vote':vote})
df


# In[33]:


#name and vote cant scrap by me please teach me that


# In[34]:


df.head()


# In[35]:


df.tail(10)


# In[38]:


df.sample(20)


# # Q-6

# In[2]:


from bs4 import BeautifulSoup
import requests


# In[7]:


page = requests.get('https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-greycompare')
page


# In[8]:


soup=BeautifulSoup(page.content)
soup


# In[13]:


bookname = soup.find('tr',class_="table-cell-10943-0-1")
bookname


# In[14]:


#this page cant be scrap because this shows response 404


# # q-8

# In[24]:


import pandas as pd
import selenium
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[25]:


driver=webdriver.Chrome(r"chromedriver.exe")


# In[26]:


driver.get("https://archive.ics.uci.edu/")


# In[28]:


alldataset=driver.find_element(By.XPATH,"/html/body/table[1]/tbody/tr/td[2]/span[2]/a")
alldataset.click()


# In[30]:


Dataset_name=[]
Data_type=[]
Task=[]
Attribute_type=[]
No_of_instances=[]
No_of_attribute=[]
Year=[]


# In[81]:


Dataset_name=driver.find_elements(By.XPATH,'//p[@class="normal"]')
for i in Dataset_name[0:10]:
    title=i.text
    Dataset_name.append(title)


# In[82]:


Data_type=driver.find_elements(By.XPATH,)
for i in Data_type[0:10]:
    title=i.text
    Data_type.append(title)


# In[83]:


print(len(Dataset_name),len(Data_type))


# In[79]:


Data_type


# In[80]:


Dataset_name


# # q-9

# In[84]:


import pandas as pd
import selenium
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[89]:


driver=webdriver.Chrome(r"chromedriver.exe")


# In[90]:


driver.get("https://www.naukri.com/")


# In[91]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('data science')


# In[93]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/input")
location.send_keys('bangalore')


# In[94]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[95]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[96]:


title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)


# In[97]:


location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)


# In[98]:


company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company_name)


# In[99]:


experience_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags[0:10]:
    exp=i.text
    experience_required.append(exp)


# In[100]:


print(len(job_title),len(job_location),len(company),len(experience_required))


# In[101]:


import pandas as pd
df=pd.DataFrame({'title':job_title,'location':job_location,'company_name':company_name,'experience':experience_required})
df


# # q-3

# In[11]:


import pandas as pd
import selenium
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[12]:


driver=webdriver.Chrome(r"chromedriver.exe")


# In[13]:


driver.get('https://www.statisticstimes.com/economy/india/indian-states-gdp.php')


# In[14]:


#A) Rank
#B) State
#) GSDP(18-19)- at current prices
#D) GSDP(19-20)- at current prices
#E) Share(18-19)
#F) GDP($ billion)


# In[16]:


Rank=[]
State=[]
GSDP18=[]
GSDP19=[]
Share=[]
GDP=[]


# In[36]:


Rank=driver.find_elements(By.XPATH,'//td[@class="data1"]')
for i in Rank [0:10]:
    location=i.text
    Rank.append(Rank)


# In[37]:


Rank


# In[38]:


print(len(Rank))


# In[39]:


State=driver.find_elements(By.XPATH,'//td[@class="name"]')
for i in State [0:10]:
    location=i.text
    State.append(State)


# In[40]:


State


# In[41]:


print(len(State))


# In[42]:


GSDP18=driver.find_elements(By.XPATH,'//td[@class="data"]')
for i in GSDP18 [0:10]:
    location=i.text
    GSDP18.append(GSDP18)


# In[43]:


print(len(GSDP18))


# In[44]:


#q 3 is vety difficult for me please teach me how to scrap this type of page.


# # Q-4

# In[62]:


import pandas as pd
import selenium
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[63]:


driver=webdriver.Chrome(r"chromedriver.exe")


# In[64]:


driver.get("https://github.com/trending")


# In[65]:


Repository_title=[]
Repository_description=[]
Contributors_count=[]
Language_used=[]


# In[66]:


Repository_title=driver.find_elements(By.XPATH,'//h1[@class="h3 lh-condensed"]')
for i in Repository_title[0:10]:
    title=i.text
    Repository_title.append(title)


# In[77]:


print(len(Repository_title))


# In[140]:


Repository_description=driver.find_elements(By.XPATH,'//div[@class="f6 color-fg-muted mt-2"]')
for i in Repository_description[0:10]:
    title=i.text
    Repository_description.append(title)


# In[141]:


print(len(Repository_description))


# In[142]:


Contributors_count=driver.find_elements(By.XPATH,'//span[@class="d-inline-block float-sm-right"]')
for i in Contributors_count[0:10]:
    title=i.text
    Contributors_count.append(title)


# In[143]:


print(len(Contributors_count))


# In[167]:


Language_used=driver.find_elements(By.XPATH,'//div[@class="f6 color-fg-muted mt-2"]')
for i in Language_used[0:10]:
    title=i.text
    Language_used.append(title)


# In[168]:


print(len(Language_used))


# In[169]:


Language_used


# In[170]:


print(len(Repository_title),len(Repository_description),len(Contributors_count),len(Language_used))


# In[171]:


import pandas as pd
df=pd.DataFrame({'title':Repository_title,'description':Repository_description,'count':Contributors_count,'Language_used':Language_used})
df


# In[172]:


df.tail(10)


# # q-5

# In[173]:


import pandas as pd
import selenium
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[174]:


driver=webdriver.Chrome(r"chromedriver.exe")


# In[175]:


driver.get("https://www.billboard.com/charts/")


# In[178]:


billboard=driver.find_element(By.CLASS_NAME,"c-label  ")
billboard.click()


# In[179]:


Song_name=[]
Artist_name=[]
Last_week_rank=[]
Peak_rank=[]
Weeks_on_board=[]


# In[225]:


Song_name=driver.find_elements(By.XPATH,'//span[@class_="c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet"]')
for i in Song_name[0:10]:
    name=i.text
    Song_name.append(title)


# In[226]:


Song_name


# In[227]:


print(len(Song_name))


# In[ ]:




