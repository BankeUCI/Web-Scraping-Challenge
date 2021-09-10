from bs4 import BeautifulSoup
from splinter import Browser
import time
def scrape_info():
    executable_path = {"executable_path": "C:\Drivers\Chromedriver_win32\chromedriver"}
    #browser = Browser("chrome", **executable_path, headless=False)
    browser = Browser("chrome", executable_path="C:\Drivers\Chromedriver_win32\chromedriver", headless=False)
    time.sleep(1)
    #return {}
    url_news = "https://redplanetscience.com/"
    browser.visit(url_news)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news_title = soup.find_all('div', class_ = 'content_title')[0].get_text()
    news_paragraph = soup.find_all('div', class_ = 'article_teaser_body')[0].get_text()
    news_date = soup.find_all('div', class_ = 'list_date')[0].get_text()
    print(news_date)
    print(news_title)
    print('------------------------------------------')
    print(news_paragraph)
    url_spaceimage = "https://spaceimages-mars.com/"
    browser.visit(url_spaceimage)
    xpath = '/html/body/div[1]/img'
    results = browser.find_by_xpath(xpath)
    img = results[0]
    img.click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image_url = soup.find("img", class_="headerimage")["src"]
    featured_image_url = url_spaceimage + image_url
    featured_image_url
    import requests
    featured_image_url = url_spaceimage + image_url
    response = requests.get(featured_image_url, stream=True)
    file = open("Image.png", "wb")
    file.write(response.content)
    file.close()
    import pandas as pd
    url_mars = 'https://galaxyfacts-mars.com'
    table = pd.read_html(url_mars)
    table
    table_df = table[0]
    table_df.head()
    table2_df = table[1]
    table2_df.head(10)
    mars_facts = table2_df.rename(columns={0:"Mars Profile", 1:"Metric"})
    mars_facts
    html_table = mars_facts.to_html()
    html_table
    html_table.replace('\n', '')
    mars_facts.to_html('table.html')
    url_hemisphere = 'https://marshemispheres.com/'
    browser.visit(url_hemisphere)
    html_hemisphere = browser.html
    soup = BeautifulSoup(html_hemisphere, "html.parser")
    hemispheres = soup.find_all("div", class_="item")
    hemispheres_info = []
    hemispheres_url = "https://marshemispheres.com/"
    for info in hemispheres:
        title = info.find("h3").text
        hemispheres_img = info.find("a", class_="itemLink product-item")["href"]
        browser.visit(hemispheres_url + hemispheres_img)
    image_html = browser.html
    web_info = BeautifulSoup(image_html, "html.parser")
    img_url = hemispheres_url + web_info.find("img", class_="wide-image")["src"]
    dictionary = {"title" : title, "img_url" : img_url}
    hemispheres_info.append(dictionary)
    print(hemispheres_info)
    html_hemisphere = browser.html
    soup = BeautifulSoup(html_hemisphere, "html.parser")
    hemispheres = soup.find_all("div", class_="item")
    hemispheres_info = []
    hemispheres_url = "https://marshemispheres.com/"
    for info in hemispheres:
        title = info.find("h3").text
        hemispheres_img = info.find("a", class_="itemLink product-item")["href"]
        browser.visit(hemispheres_url + hemispheres_img)
        image_html = browser.html
        web_info = BeautifulSoup(image_html, "html.parser")
    img_url = hemispheres_url + web_info.find("img", class_="wide-image")["src"]
    hemispheres_info.append({"title" : title, "img_url" : img_url})
    print("")
    print(title)
    print(img_url)
    print("------------------------------------")
    browser.quit()
    if __name__ == "__main__":
        scrape_info()