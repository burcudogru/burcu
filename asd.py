from bs4 import BeautifulSoup
import requests

r = requests.get("https://mlab.com/login/")
html = BeautifulSoup(r.text)
print(html.find("title").text)
