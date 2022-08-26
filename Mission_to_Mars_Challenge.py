#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


import pandas as pd


# In[3]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[5]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[6]:


slide_elem.find('div', class_='content_title')


# In[7]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[8]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[9]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[10]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[11]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[12]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[13]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[14]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[15]:


df.to_html()


# In[16]:


browser.quit()


# In[17]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[18]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[19]:


# ### Visit the NASA Mars News Site


# In[20]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[21]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[22]:


slide_elem.find('div', class_='content_title')


# In[23]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[24]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# In[25]:


# ### JPL Space Images Featured Image


# In[26]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[27]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[28]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[29]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[30]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[31]:


# ### Mars Facts


# In[32]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[33]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[34]:


df.to_html()


# In[35]:


# ### D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles


# In[36]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[37]:


list = [90,70,65,55]
score_list = []
for i in list:
    dict={}
    if i>=70:
        dict["score"]="pass"
    else:
        dict["score"]="fail"
    score_list.append(dict)
    print(score_list)


# In[45]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
links = browser.find_by_css('a.product-item img')
for i in range(len(links)):
    hemisphere={}
    browser.find_by_css('a.product-item img')[i].click()
    
    # pulling in sample image URL
    sample_element=browser.links.find_by_text("Sample").first
    hemisphere["image_url"]=sample_element["href"]
    
    # creating title for images
    image_title=browser.find_by_css('h2.title').text
    hemisphere["image_title"]=image_title
    
    # Appending temporary dictionary to hemisphere_image_urls list
    hemisphere_image_urls.append(hemisphere)
    
    browser.back()


# In[46]:


# 4. Print the list that holds the dictionary of each image url and title. #each hemisphere URL and image type
print(hemisphere_image_urls)


# In[47]:


# 5. Quit the browser
browser.quit()

