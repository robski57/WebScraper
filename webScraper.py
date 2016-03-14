import requests
from bs4 import BeautifulSoup
#place web address below
url = "https://weather.com/weather/today/l/USDC0001:1:US"

r = requests.get(url)

soup = BeautifulSoup(r.content)

links = soup.find_all("a")

for link in links:
    print("<a href='%s'>%s</a>"%(link.get("href"), link.text))


g_data = soup.find_all("div", {"class": "info"})

for item in g_data:
    print (item.contents[0].find_all("a", {"class": "city=name"})[0].text)
    print (item.contents[1].find_all("p", {"class": "City"})[0].text)
    try:
        print (item.contents[1].find_all("li", {"class": "primary"})[0].text)
    except:
        pass
