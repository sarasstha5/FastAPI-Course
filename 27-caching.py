
# Caching using TTL(Time-To-Live) method.here time matters for caching. If the data is fetched within the TTL time then it will use the cached data otherwise it will fetch the data from the third party url.
from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import time

app = FastAPI()
cach_data = []
last_fetch = 0

@app.get("/news")
def get_news():
    global cach_data,last_fetch
    start = time.time()
    if time.time() - last_fetch > 60:  #cache for 60 seconds
        url = "https://www.sidhakura.com"    #third party url
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")  #web crawling

        for links in soup.find_all("span", class_ = "titles title-7 title-small"):
            cach_data.append(links.text)

        last_fetch = time.time()

    else:
        print("Using cached data")

    end = time.time()

    return{ 
        "headlines":cach_data,
        "time_taken":end-start
    }