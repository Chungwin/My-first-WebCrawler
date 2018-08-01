import requests
from bs4 import
from urllib.parse import urljoin
import time


class CrawledArticle():
    def __init__(self, tiitle, emoji, content, image):
        self.title = title
        self.emoji = emoji
        self.content = content
        self.image = image


class ArticleFetcher():
    def fetch(self):
        url = "http://python.beispiel.programmierenlernen.io/index.php"

        while url != "":
            print(url)
            time.sleep(2)
            r = requests.get(url)
            doc = BeautifulSoup(r.text, "html.parser")

            for card in doc.select(".card"):
                emoji = card.select_one(".emoji").text
                content = card.select_one(".card-text").text
                title = card.select(".card-title span")[1].text
                image = urljoin (url, card.select_one("img").attrs["src"])

                yield CrawledArticle(title, emoji, content, image)

            next_button = doc.select(".navigation .btn")
            if next_button:
                next_href = next_button.attrs["href"]
                next_href = urljoin(url, next_href)
                url = next_href
            else:
                url = ""


fetcher = ArticleFetcher()

# Now we can say e.g: Stop scraping after 8 articles ... 
counter = 0
for article in fetcher.fetch():
    if counter == 8:
        break
    counter = counter + 1
    print("Title: " + article.title)
