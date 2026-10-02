#Pagination means dividing a large amount of data into smaller pages instead of returning everything at once.
from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()
headlines = []

@app.get("/news")
def get_news(page:int =1, limit:int = 5):
    url = "https://www.sidhakura.com"    #third party url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")  #web crawling
    skip = (page - 1) * limit

    for links in soup.find_all("span", class_ = "titles title-7 title-small"):
        headlines.append(links.text)

    return{ 
        "headlines":headlines[skip:skip + limit]
    }