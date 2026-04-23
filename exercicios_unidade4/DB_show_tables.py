import mysql.connector

bd = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1010',
    database='primeirobanco'
)

cursor = bd.cursor()

sql = 'SHOW TABLES'

cursor.execute(sql)

resultado = cursor.fetchall()

for linha in resultado:
    print(linha)
