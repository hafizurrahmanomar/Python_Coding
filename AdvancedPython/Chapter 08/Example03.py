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
            <h1 id="h">Faisal</h1>
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
print(soup.find_all("h1",{'id':'h'}))

# You can use Beautiful Soup to find elements on a web page that have specific attributes. 
