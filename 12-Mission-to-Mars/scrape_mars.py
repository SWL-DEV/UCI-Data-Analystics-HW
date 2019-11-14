# Import dependencies
from bs4 import BeautifulSoup 
from splinter import Browser
import pandas as pd 
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

# Create dictionary to append findings
mars_update = {}

def mars_news():
    browser = init_browser

    # Visit Nasa's news site
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
   
    # Find the contents that has the news
    results = soup.find_all('li', class_='slide')

    for result in results:
        try:
            title = result.find('div', class_='content_title').text
            para_text = result.find('div', class_='article_teaser_body').text

        mars_update['title'] = title
        mars_update['para_text'] = para_text

    # Close browser after scraping
    browser.quite()

    # Return results
    return mars_update



def mars_image():
    browser = init_browser

    # Visit JPL website
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Featured image content is in the footer
    footer = soup.find('footer')
    feature_image_url = f'https://www.jpl.nasa.gov' + footer.find('a')['data-fancybox-href']

    mars_update['feature_image_url'] = feature_image_url

    # Close browser after scraping
    browser.quit()

    # Return results
    return mars_update




def mars_weather():
    browser = init_browser

    # Visit Mars Weather's Twitter account
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Find all contents that include the 
    contents = soup.find_all('div', class_='js-tweet-text-container')

    for content in contents:    
        mars_weather = content.find('p', class_='TweetTextSize').text
        if 'InSight' in mars_weather:
                
            print('--------------------')
            print(mars_weather)
        else:
            pass

    mars_update['mars_weather'] = mars_weather

    # Close browser after scraping
    browser.quite()

    # Send updated info into dictionary
    return mars_update