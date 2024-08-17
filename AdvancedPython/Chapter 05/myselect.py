import pymysql

connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password ="",
    db= "jafricode_database"
    )

cursor = connection.cursor()
sql = "SELECT u_name FROM student WHERE u_city!= %s AND u_id > %s "
data = ('DIKHAN',100)
cursor.execute(sql, data)

records = cursor.fetchall()


for record in records:
    for data in record:
        print(data)
connection.close()
