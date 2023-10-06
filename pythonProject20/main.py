import requests
from bs4 import BeautifulSoup

# specify the URL to scrape
url = 'https://www.ispringsolutions.com/blog/best-online-learning-platforms'

# send a request to the URL and get the HTML response
response = requests.get(url)

# parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# find all the links on the page and print them
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
