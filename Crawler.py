# Download html code from URL
import requests
from bs4 import
from urllib.parse import urljoin


class CrawledArticle():
    def __init__(self, tiitle, emoji, content, image):
        self.title = title
        self.emoji = emoji
        self.content = content
        self.image = image


# Whole fetcher is now in class ArticleFetcher()
class ArticleFetcher():
    def fetch(self):
        url = "http://python.beispiel.programmierenlernen.io/index.php"
        r = requests.get(url)
        doc = BeautifulSoup(r.text, "html.parser")

        articles = []
        for card in doc.select(".card"):
            emoji = card.select_one(".emoji").text
            content = card.select_one(".card-text").text
            title = card.select(".card-title span")[1].text
            image = urljoin (url, card.select_one("img").attrs["src"])

            crawled = CrawledArticle(title, emoji, content, image)
            articles.append(crawled)

        return articles


fetcher = ArticleFetcher()
# Start fetching everything into the list
articels = fetcher.fetch()
# Outputs a list of objects
print(articles)


# Outfuts full URL of image because of urljoin
for article in articles:
    print(article.image)
