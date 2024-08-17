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

        <ul>
        <li>Item1</li>
        <li>Item2</li>
        <li>Item3</li>
        <li>Item4</li>

        </ul>

    </body>

</html>


"""

soup = BeautifulSoup(html_content, 'html.parser')
all_p = soup.find_all('p')
for p in all_p:
    print(p.text)


all_li = soup.find_all('li')
for li in all_li:
    print(li.text)


# Extracting text: You can use Beautiful Soup to extract text from HTML elements such as headings, paragraphs, and lists. 
