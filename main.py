from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import re
import random

randNumb = random.randint(0, 1001)

URL = "https://1000mostcommonwords.com/1000-most-common-romanian-words/"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

soup.prettify("utf-16")

def remove_tags(text):
  clean = re.compile('<.*?>')
  return re.sub(clean, "", text)

tr = [remove_tags(str(element)) for element in soup.find_all("tr")[randNumb]]
words = [tr[3], tr[5]]

# Make Unsplash API call\
secretKey = "kdyOkMnL1o-iOm1yjW9enuJ5gMEBuEGTs4fytBoYnf4"
response = requests.get(f"https://api.unsplash.com/search/photos?per_page=5&query={tr[5]}&client_id={secretKey}")


img = response.json()["results"][1]["urls"]["full"]

print(words)

app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route("/")
def home():
  return render_template("index.html", data=[words, img])

if __name__ == "__main__":
  app.run()