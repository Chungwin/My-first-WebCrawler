# Download html code from URL
import requests
r = requests.get("http://python.beispiel.programmierenlernen.io/index.php")
# Save it in doc variable
from bs4 import BeautifulSoup
doc = BeautifulSoup(r.text, "html.parser")

# This class covers now all our crawled data: title, emoji, content, image
class CrawledArticle():
    def __init__(self, tiitle, emoji, content, image):
        self.title = title
        self.emoji = emoji
        self.content = content
        self.image = image

# Create a list with intention to append all CrawledArticle here
articles = []

# All infos we want to crawl are in a <div class="card">
for card in doc.select(".card"):
    emoji = card.select_one(".emoji").text
    content = card.select_one(".card-text").text
    title = card.select(".card-title span")[1].text
    image = card.select_one("img").attrs["src"]

    # Append CrwaledArticle to artice to articles-list
    crawled = CrawledArticle(title, emoji, content, image)
    articles.append(crawled)

    print(crawled)
    # Outputs list of article objects

    print(crawled.title)
    # Outputs just titles of crawled articles
