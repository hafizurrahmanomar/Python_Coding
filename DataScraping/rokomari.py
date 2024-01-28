## Terminal open than=>
## 1. pip install beautifulsoup4
## 1. pip install requests
## Than import 
import requests
from bs4 import BeautifulSoup

rokomari_url = "https://www.rokomari.com/book"

my_request = requests.get(rokomari_url)
## if  result => Download Rokomari status 200 => Than code successful run
# print("Download Rokomari status",my_request.status_code)
# ## result => HTML Code here
# print(my_request.content)

soup = BeautifulSoup(my_request.content,"html.parser")
# print(soup)
all_books = soup.find_all("div",class_="book-list-wrapper")
# print("all_books",all_books)

Book_lists = []

for book in all_books:
    book_title=book.find('p',class_="book_title")
    book_author=book.find('p',class_="book_author")
    book_price=book.find('p',class_="book_price")
    
    book_dict={
        "title":book_title,
        "author":book_author,
        "price":book_price,
    }
    Book_lists.append(book_dict)

print(Book_lists)

