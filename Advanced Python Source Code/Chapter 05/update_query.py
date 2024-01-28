import pymysql

connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password ="",
    db= "jafricode_database"
    )

cursor = connection.cursor()

# sql = "UPDATE student SET u_city = 'Paharpur' WHERE u_id = 11 OR u_id = 22 "
sql = "UPDATE student SET u_city = %s WHERE u_id = %s OR u_id = %s "
data = ('Peshawar', 100, 101)
cursor.execute(sql, data)
connection.commit()
connection.close()