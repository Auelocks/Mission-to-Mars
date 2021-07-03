# Mission-to-Mars

This project uses Python and Jupyter Notebook scripts to create an informative Mars web app that is dynamic and mobile-responsive using BeautifulSoup and Splinter to scrape Mars data, the latest news, and full-resolution images with their respective titles. Scraped data is stored on a Mongo database, and displayed using html format with Bootstrap components to stylize the web app.

## Important Files
 * Mission_to_Mars_Challenge.py
 * scraping.py
   * code retrieves real-time web data and images; used to integrate MongoDB with web app
 * app.py
   * code using Flask and Mongo to create web app
 * index.html
   * code will display the web app data/images
