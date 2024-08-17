import pymysql

connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password ="",
    db= "jafricode_database"
    )
cursor = connection.cursor()

# sql = "SELECT * FROM student ORDER BY u_id ASC LIMIT 3"
sql = "SELECT * FROM student LIMIT 3 OFFSET 2"

cursor.execute(sql)
results = cursor.fetchall()

for rslt in results:
    print(rslt)

connection.commit()
connection.close()