from bs4 import BeautifulSoup

html_content = """
<html>
    <head>
        <title> Website Title</title>   
        <style>
            div{
                background-color: red;
                width:200px;
                height: 400px; 
            }
            div h1 {
                color:white;
            }
        </style>
    

    </head>
    <body>
       <h1>Welcome to our website</h1> 
        <h1>Welcome to our website</h1> 

       <p>This is the paragraph.. Website is created by Faisal ZAMIR</p>
       <h2>JafriCode</h2>
       <h3>Faisal Zamir</h3>
        <a href="https://www.jafricode.com">JafriCode</a>

        <div>
            <h1>Block</h1>
        </div>
        <img src="1.png" alt="" width="50" height="50">
    </body>

</html>


"""

soup = BeautifulSoup(html_content, 'html.parser')
para = soup.p.string
print(para)