import requests
from bs4 import BeautifulSoup
url = "https://www.jafricode.com/"


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
response = requests.get(url, headers=headers)
# response = requests.get(url)
soup  = BeautifulSoup(response.content, 'html.parser')
print(soup.find('img').attrs)