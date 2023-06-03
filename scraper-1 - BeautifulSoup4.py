import requests
from bs4 import BeautifulSoup

def get_malayalam_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the div with the specified class and id
    article = soup.find('div', class_='article-content no-border', id='mainArticleContent')
    if article:
        text = ' '.join([p.text for p in article.find_all('p')])
        return text
    else:
        return 'Could not find article body.'

url = "https://www.asianetnews.com/entertainment-news/bigg-boss-malayalam-season-5-is-akhil-marar-evicted-from-bb-house-fans-reaction-on-social-media-vvk-rvolmr"
print(get_malayalam_news(url))
