'''first need to install mysql-connector using pip'''

import mysql.connector

mydb = mysql.connector.connect(
    host='Your_hoatname', user='your_username', passwd='Your_password', database='Your_database_name')
# host, user, passwd should be this format otherwise it will give an error

mycursor = mydb.cursor()

mycursor.execute("show databases")
for i in mycursor:
    print(i)
print()
print()
cur = mydb.cursor()
cur.execute("select * from student")
# you can also save data to other place
result = cur.fetchall()  # you can also fetch one data using fetchone
for i in result:
    print(i)
