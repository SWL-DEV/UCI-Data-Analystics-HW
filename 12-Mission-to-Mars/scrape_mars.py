# Import dependencies
from bs4 import BeautifulSoup 
from splinter import Browser
import pandas as pd 
import time

# Create dictionary to append findings
mars_update = {}

# Initial call to everything or every function HEERRREE
def scrape():
    browser = init_browser()

    mars_news(browser)
    mars_image(browser)
    mars_weather(browser)
    mars_facts(browser)
    mars_hemispheres(browser)

    close_browser(browser)

    return mars_update


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def close_browser(browser):
    browser.quit()

def mars_news(browser):
    # Visit Nasa's news site
    news_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(news_url)

    time.sleep(1)

    # Scrape page into Soup
    news_html = browser.html
    soup = BeautifulSoup(news_html, 'html.parser')
   
    # Find the contents that has the news
    results = soup.find_all('li', class_='slide')

    for result in results:
        try:
            title = result.find('div', class_='content_title').text
            para_text = result.find('div', class_='article_teaser_body').text

            mars_update['title'] = title
            mars_update['para_text'] = para_text
        except AttributeError as e:
            print(e)

    # Return results
    return mars_update

def mars_image(browser):
    # Visit JPL website
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)

    time.sleep(1)

    # Scrape page into Soup
    jpl_html = browser.html
    soup = BeautifulSoup(jpl_html, 'html.parser')

    # Featured image content is in the footer
    footer = soup.find('footer')
    feature_image_url = f'https://www.jpl.nasa.gov' + footer.find('a')['data-fancybox-href']

    mars_update['feature_image_url'] = feature_image_url

    # Return results
    return mars_update

def mars_weather(browser):
    # Visit Mars Weather's Twitter account
    weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)

    time.sleep(1)

    # Scrape page into Soup
    weather_html = browser.html
    soup = BeautifulSoup(weather_html, 'html.parser')

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

    # Send updated info into dictionary
    return mars_update

def mars_facts(browser):
    # Retrieve table on the site with read_html
    table = pd.read_html('https://space-facts.com/mars/')

    # Convert table into dataframe
    df = table[0]

    # Rename headers
    df.columns=['','Value']

    # Convert dataframe to html
    html_table = df.to_html(index=False)

    # Drop line breaks
    pretty_html = html_table.replace('\n', '')

    # # Save new html table
    df.to_html('templates/table.html', index=False)

    mars_update['mars_facts'] = pretty_html

    # Save the html code for table to dictionary
    return mars_update

def mars_hemispheres(browser):
    # Visit the USGS website
    usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(usgs_url)

    time.sleep(1)

    # Scrape page into Soup
    usgs_html = browser.html
    soup = BeautifulSoup(usgs_html, 'html.parser')

    items = soup.find_all('div', class_='item')

    hemisphere_image_urls=[]

    usgs_url = 'https://astrogeology.usgs.gov/'

    for item in items:
        
        # Save name of the image
        title = item.find('h3').text
        
        # Find the href to the corresponding image
        image_href = item.find('a', class_='itemLink product-item')['href']
        
        # Complete the url to site that has the full resolution image link
        new_link_url = usgs_url + image_href
        
        # Visit the new link the now complete link
        browser.visit(new_link_url)
        new_link_html = browser.html
        
        # Parse through the individual product site
        soup = BeautifulSoup(new_link_html, 'html.parser')
        
        # Look for the full resolution image link
        destination = soup.find('div', class_='downloads')
        full_res_url = destination.find('a')['href']

        # Save results to the image_urls dictionary
        hemisphere_image_urls.append({'title':title, 'image_url': full_res_url})
    
        mars_update['hemisphere_image_urls'] = hemisphere_image_urls
        
    return mars_update