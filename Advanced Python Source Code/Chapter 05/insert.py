import pymysql

connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password ="",
    db= "jafricode_database"
    )
cursor = connection.cursor()
# sql = "INSERT INTO student(u_id, u_name, u_city) VALUES (11, 'Jafri', 'DIKHAN'),(23, 'Zamir','Lahore'), (22, 'Ali','Karachi')"
# sql = "INSERT INTO student(u_id, u_name, u_city) VALUES (%s, %s, %s)"
# values = [
# (101, "Kamran", "Lahore"),
# (102, "John", "DIKHAN"),
# (103, "Jafri", "London")

# ]
# cursor.executemany(sql, values)
connection.commit()
connection.close()