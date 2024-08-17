from bs4 import BeautifulSoup

html_content = """
<html>
    <head>
        <title> Website Title</title>   
    </head>
    <body>
       <h1 class = "para">Welcome to our website</h1> 
       <p>This is the paragraph.. Website is created by Faisal ZAMIR</p>
       <h2>JafriCode</h2>
       <h3>Faisal Zamir</h3>
        <a href="https://www.jafricode.com">Faisal</a>

        <div>
            <h1>Faisal</h1>
            <h1 class="heading">Block 2</h1>
            <h1 class = "heading">Block 3</h1>
            <h1>Block 4</h1>

        </div>
        <img src="1.png" alt="" width="50" height="50">
        <p>Faisal</p>
        <p>Faisal</p>
        <p>Jafri</p>

    </body>

</html>


"""

soup = BeautifulSoup(html_content, 'html.parser')
# all_h1 =soup.find_all('h1')
# for i in all_h1:
#     print(i.text)

# result = soup.find_all('h1', {'class': 'heading'})
# for i in result:
#     print(i.text)

# results = soup.find_all(string='Faisal')
# print(results)
# for i in results:
#     print(i)


# print(soup.find('a')['href'])

print(soup.find('h1').attrs)

"""
soup.find('h1')
soup.find('h1').text
soup.find_all('div', {'class': 'container'})
soup.find_all(text='Hello, world!')
soup.find('a')['href']
soup.find('img').attrs
"""