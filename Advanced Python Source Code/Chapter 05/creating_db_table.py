import pymysql

connection = pymysql.connect(
    host ="localhost",
    user = "root",
    password=  "",
    db = "jafricode_database"
)
cursor = connection.cursor()
# sql1  = "CREATE DATABASE jafricode_database"
# cursor.execute(sql1)

# sql2 = "USE jafricode_database"
# cursor.execute(sql2)

# sql3 = "CREATE TABLE users(u_id INT AUTO_INCREMENT PRIMARY KEY, u_name VARCHAR(200))"
# cursor.execute(sql3)

sql4 = "CREATE TABLE student(u_id INT AUTO_INCREMENT PRIMARY KEY, u_name VARCHAR(200), u_city VARCHAR(100))"
cursor.execute(sql4)

connection.commit()
connection.close()