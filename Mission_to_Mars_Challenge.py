# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Featured Articles

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# Featured Images

# Visit space images URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL for the image created above
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# Scrape Mars facts from table into Pandas table
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

# Prepare html ready dataframe
df.to_html()

# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

### Hemispheres

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range (0,4):
    hemispheres = {}
    find_image = browser.find_by_css('a.product-item img')[i].click()
    click_sample = browser.find_by_text('Sample').click()
    # Parse the resulting html with soup
    imgs_soup = soup(browser.html, 'html.parser')
    # Find the relative image url
    rel_img_url = imgs_soup.find_all('img')[4].get('src')
    # Find the image title
    rel_img_title = imgs_soup.find("h2").contents[0]
    # Use the base URL to create an absolute URL for the image created above
    img_url = f'https://marshemispheres.com/{rel_img_url}'
    # add url, title to dictionary
    hemispheres['img_url'] = img_url
    hemispheres['img_title'] = rel_img_title
    # add dictionary to list
    hemisphere_image_urls.append(hemispheres)
    
    browser.back()
    i+=1

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

browser.quit()

