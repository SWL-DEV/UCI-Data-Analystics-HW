# Import dependencies
from bs4 import BeautifulSoup 
from splinter import Browser
import pandas as pd 
import requests 


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def mars_news():
    browser = init_browser

    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
   
 
    results = soup.find_all('div', class_='image_and_description_container')

    for result in results:
        # Retrieve parent divs for all articles
        title = result.find('div', class_='content_title').text

        # Scrape the paragraph text
        para_text = result.find('div', class_='article_teaser_body').text

    return title, para_text


def mars_image():
    browser = init_browser

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Featured image content is in the footer
    footer = soup.find('footer')
    feature_image_url = f'https://www.jpl.nasa.gov' + footer.find('a')['data-fancybox-href']

    return feature_image_url


def mars_weather():
    browser = init_browser

    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    contents = soup.find_all('div', class_='content')
    mars_weather = content.find('p', class_='TweetTextSize').text

    return mars_weather