import pymysql

connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password ="",
    db= "jafricode_database"
    )

cursor = connection.cursor()
sql = "DELETE FROM student where u_city = %s "
data = ('DIKHAN',)
cursor.execute(sql, data)
connection.commit()
connection.close()