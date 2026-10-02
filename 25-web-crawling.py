# usually in python
# from bs4 import BeautifulSoup
# import requests
# url = "https://example.com"
# response = requests.get(url)

# soup = BeautifulSoup(response.text , "html.parser")

# for link in soup.find_all("a"):  #a = <a> in html
#     print(link.get("href"))

from fastapi import FastAPI
import requests 
from bs4 import BeautifulSoup

app = FastAPI()
Bulletins = []

@app.get("/crawl")
def links():
    urls = "https://ocmcm.bagamati.gov.np/category/transfer"
    response = requests.get(urls)

    soul = BeautifulSoup(response.text, "html.parser")

    for links in soul.find_all("h3"):
        Bulletins.append(links.text)

    return{
        "Headlines":Bulletins
    }
