import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user='root',
    passwd = 'VFSXFSF5'
)

#prepare cursor objecct
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE elderco")
print("Database Created!")