import pymysql

connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password ="",
    db= "jafricode_database"
    )
cursor = connection.cursor()

sql = "SELECT * FROM student where u_id > 100 AND u_city = 'London' "
cursor.execute(sql)
results = cursor.fetchall()

for r in results:
    print(r)

connection.commit()
connection.close()