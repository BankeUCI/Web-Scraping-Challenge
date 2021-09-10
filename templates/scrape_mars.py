# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Import BeautifulSoup
from bs4 import BeautifulSoup


# %%
# Import Splinter and set the chromedriver path 
from splinter import Browser
executable_path = {"executable_path": "C:\Drivers\Chromedriver_win32\chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)


# %%
import pandas as pd
import requests


# %%
# Visit the following URL
url_news = "https://redplanetscience.com/"
browser.visit(url_news)


# %%
# HTML Object
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# %%
# Scrape the latest News Title and Paragraph text
news_title = soup.find_all('div', class_ = 'content_title')[0].get_text()

news_paragraph = soup.find_all('div', class_ = 'article_teaser_body')[0].get_text()

news_date = soup.find_all('div', class_ = 'list_date')[0].get_text()

print(news_date)
print(news_title)
print('------------------------------------------')
print(news_paragraph)

# %% [markdown]
# # JPL Mars Space Images - Featured Image

# %%
from bs4 import BeautifulSoup


# %%
# Import splinter and set the chromedriver path
from splinter import Browser
executable_path = {"executable_path": "C:\Drivers\Chromedriver_win32\chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)


# %%
#Visit the url
url_spaceimage = "https://spaceimages-mars.com/"
browser.visit(url_spaceimage)


# %%
# xpath selector to grab for featured image
xpath = '/html/body/div[1]/img'


# %%
# Using splinter to click the featured image
# to get the full resolution image
results = browser.find_by_xpath(xpath)
img = results[0]
img.click()


# %%
# Scrape the browser into soup and use soup to find the full resolution image
# Save the image to a variable called 'image_url'
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
image_url = soup.find("img", class_="headerimage")["src"]
featured_image_url = url_spaceimage + image_url
featured_image_url


# %%
# using the requests library to download and save the image from the 'image_url'
import requests

featured_image_url = url_spaceimage + image_url
response = requests.get(featured_image_url, stream=True)
file = open("Image.png", "wb")
file.write(response.content)
file.close()



# %%
# Using shutil to save image
import requests
import shutil
response = requests.get(featured_image_url, stream=True)
with open('/img2.png', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)


# %%
# Display the image with IPython.display
#from IPython.display import image
#import requests

#img = Image.open(requests.get(featured_image_url, stream=True).raw)
#image.save('img1.jpg')


# %%
# Display the image with IPython.display
from IPython.display import Image
Image(url='img.jpg')

# %% [markdown]
# # Mars Facts

# %%
import pandas as pd


# %%
url_mars = 'https://galaxyfacts-mars.com'


# %%
# Scraping tables with pandas
table = pd.read_html(url_mars)
table


# %%
# Slicing dataframes using normal indexing
table_df = table[0]
table_df.head()


# %%
# Slicing dataframes using normal indexing
table2_df = table[1]
table2_df.head(10)


# %%
# Renaming table columns and assigning to a variable
mars_facts = table2_df.rename(columns={0:"Mars Profile", 1:"Metric"})
mars_facts


# %%
# generating html table from DataFrames
html_table = mars_facts.to_html()
html_table


# %%
# removing newlines to clean up table
html_table.replace('\n', '')


# %%
# save table to an html file
mars_facts.to_html('table.html')

# %% [markdown]
# # Mars Hemispheres

# %%
# Import BeautifulSoup
from bs4 import BeautifulSoup


# %%
# Import Splinter and set the chromedriver path 
from splinter import Browser
executable_path = {"executable_path": "C:\Drivers\Chromedriver_win32\chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)


# %%
url_hemisphere = 'https://marshemispheres.com/'
browser.visit(url_hemisphere)


# %%
# HTML Object
html_hemisphere = browser.html

# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html_hemisphere, "html.parser")


# %%
# Retrieve all elements that contain image url to full resolution image
hemispheres = soup.find_all("div", class_="item")

# Create empty list
hemispheres_info = []

# assign url for loop

hemispheres_url = "https://marshemispheres.com/"

#iterate through each hemisphere information 
for info in hemispheres:
    title = info.find("h3").text
    hemispheres_img = info.find("a", class_="itemLink product-item")["href"]
    
    # Visit the link that contains the full image website
    browser.visit(hemispheres_url + hemispheres_img)
    
    # HTML object
    image_html = browser.html
    web_info = BeautifulSoup(image_html, "html.parser")
    
    # Create full image url
    img_url = hemispheres_url + web_info.find("img", class_="wide-image")["src"]
    
    dictionary = {"title" : title, "img_url" : img_url}
    
    hemispheres_info.append(dictionary)
    
    print(hemispheres_info)
    
    
    
    #h3 =info.find('h3')
    #link = h3.find('a')
    #href = link['href']
    #title = link['title']
    #print('----------------')
    #print(title)
    #print('https://marshemispheres.com/' + href)
    
    # Click the 'Next' button on each page
    #try:
        #browser.links.find_by-partial_text('next').click()
        
    #except:
        #print("Scraping Complete")


# %%
# Preferred output

# Retrieve all elements that contain image url to full resolution image
hemispheres = soup.find_all("div", class_="item")

# Create empty list
hemispheres_info = []

# assign url for loop

hemispheres_url = "https://marshemispheres.com/"

#iterate through each hemisphere informatiom 
for info in hemispheres:
    title = info.find("h3").text
    hemispheres_img = info.find("a", class_="itemLink product-item")["href"]
    
    # Visit the link that contains the full image website
    browser.visit(hemispheres_url + hemispheres_img)
    
    # HTML object
    image_html = browser.html
    web_info = BeautifulSoup(image_html, "html.parser")
    
    # Create full image url
    img_url = hemispheres_url + web_info.find("img", class_="wide-image")["src"]
    
    hemispheres_info.append({"title" : title, "img_url" : img_url})
    print("")
    print(title)
    print(img_url)
    print("------------------------------------")


# %%
browser.quit()


# %%



