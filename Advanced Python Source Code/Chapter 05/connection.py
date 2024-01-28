import pymysql

connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password ="",
    db= "myschooldkl"
    )
if connection:
    print("Connection is okay")
else:
    print("Connection problem")