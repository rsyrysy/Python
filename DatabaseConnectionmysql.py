import mysql.connector

db =  mysql.connector.connect(host="localhost", # Host, usually localhost
                     user="username", # your username
                     password="password", # your password
                     db="databasename") # name of the data base
#create a Cursor object.
cur = db.cursor()
# Write SQL statement here
cur.execute("select * from student")
result=cur.fetchall()
# print all the first and second cells of all the rows
for row in result :
    print (row)