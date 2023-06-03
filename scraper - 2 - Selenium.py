from selenium import webdriver
from bs4 import BeautifulSoup

def save_text_to_file(text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)


def scrape_malayalam_news(url):
    # Set up webdriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Ensure GUI is off
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    
    # Get webpage
    driver.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find the div with the specified class
    article_div = soup.find('div', class_='PostBody postbodyneww tbl-forkorts-article tbl-forkorts-article-active')
    
    if article_div:
        # Extract the article text
        article_text = ' '.join([tag.text for tag in article_div.find_all(['p', 'h1', 'h2', 'h3', 'h4'])])
        if article_text:
            save_text_to_file(article_text, 'article.txt')
            print("Article text saved successfully.")
        else:
            print("Failed to retrieve the news article.")
    else:
        print('Could not find article body.')
        
    # Quit the driver
    driver.quit()

# URL of the Malayalam news article
url = "https://www.asianetnews.com/entertainment-news/bigg-boss-malayalam-season-5-is-akhil-marar-evicted-from-bb-house-fans-reaction-on-social-media-vvk-rvolmr"

# Scrape the news article
scrape_malayalam_news(url)
