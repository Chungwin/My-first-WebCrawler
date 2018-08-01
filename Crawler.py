import requests
from bs4 import
from urllib.parse import urljoin
# Import Timer
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

            # Looping through multiple pages
            # To stop the loop, set url = ""
        while url != "":
            print(url)
            # Set a timer for the loop!! 2 sendonds ...
            time.sleep(2)
            r = requests.get(url)
            doc = BeautifulSoup(r.text, "html.parser")

            # !!! PROBLEM: Every loop overrites the list from previous loop ...
            articles = []
            for card in doc.select(".card"):
                emoji = card.select_one(".emoji").text
                content = card.select_one(".card-text").text
                title = card.select(".card-title span")[1].text
                image = urljoin (url, card.select_one("img").attrs["src"])

                crawled = CrawledArticle(title, emoji, content, image)
                articles.append(crawled)

            # When done with scraping articles from current site, select next page button
            # If there is no next page button, stop the loop
            next_button = doc.select(".navigation .btn")

            if next_button:
                next_href = next_button.attrs["href"]
                next_href = urljoin(url, next_href)
                url = next_href
            else:
                url = ""

        return articles


fetcher = ArticleFetcher()
# Start fetching everything into the list
articels = fetcher.fetch()
# Outputs a list of objects
