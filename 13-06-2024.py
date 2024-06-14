#learning how to connect python with mysql

#open command prompt and write pip3 install mysql-connector

#for connecting mysql and python or any type of language with mysql we need connector 

import mysql.connector

data=mysql.connector.connect(host="localhost",user="root",password="171119@aditya",database="demo")

print(data)

mycursor=data.cursor()

#mycursor.execute("create database demo")

'''
mycursor.execute("show databases")

for x in mycursor:
    print(x)

'''

#mycursor.execute("create table hello(helloid int primary key auto_increment,helloname varchar(40) not null,helloph int not null)")
sql="insert into hello(helloname,helloph)values(%s,%i)"
values=("aditya",9494699433)

#mycursor.execute("drop table hello")

mycursor.execute(sql,values)
