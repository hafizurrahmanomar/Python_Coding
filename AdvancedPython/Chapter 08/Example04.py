from bs4 import BeautifulSoup

html_content = """
<html>
    <head>
        <title> Website Title</title>   
    </head>
    <body>
    <table class="mytable">
            <tr>
                <td>Name</td>
                <td>Age</td>
                <td>Marks</td>
            </tr>
            <tr>
                <td>Faisal</td>
                <td>30</td>
                <td>100</td>
            </tr>
            <tr>
                <td>jAFRI</td>
                <td>20</td>
                <td>200</td>
            </tr>
        </table>
    
    </body>

</html>


"""

soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find("table")
rows = table.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    # print(cells)
    for cell in cells:
        print(cell.text)