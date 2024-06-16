#learning how to connect python with mysql

#open command prompt and write pip3 install mysql-connector

#for connecting mysql and python or any type of language with mysql we need connector 

import mysql.connector

data=mysql.connector.connect(host="localhost",user="root",password="171119@aditya",database="demo")

#print(data)

mycursor=data.cursor()
  
#mycursor.execute("create database demo")

'''
mycursor.execute("show databases")

for x in mycursor:
    print(x)

'''

#mycursor.execute("create table student(sid int primary key auto_increment,sname varchar(30) not null,age int(2) not null)")

#sql="insert into student(sname,age) values (%s,%s)"
#values=("aditya",18)

#mycursor.execute("drop table hello")

#mycursor.execute(sql,values)
#data.commit()


mycursor.execute("select * from student")
qwe=mycursor.fetchall()
for x in    qwe:
    print(x)