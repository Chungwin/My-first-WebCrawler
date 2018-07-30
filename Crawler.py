# Download html code from URL
import requests
r = requests.get("http://python.beispiel.programmierenlernen.io/index.php")
# Save it in doc variable
from bs4 import BeautifulSoup
doc = BeautifulSoup(r.text, "html.parser")

# All infos we want to crawl are in a <div class="card">
for card in doc.select(".card"):
    emoji = card.select_one(".emoji").text
    content = card.select_one(".card-text").text

    # Give me second span elements in class="card.title"
    title = card.select(".card-title span")[1].text

    # Give me the link in src attribute of img tag
    image = card.select_one("img").attrs["src"]


    print(image)
    print(title)
    print(emoji)
    print(content)

    print(card)
    break
