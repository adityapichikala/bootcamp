#learning how to connect python with mysql

#open command prompt and write pip3 install mysql-connector

#for connecting mysql and python or any type of language with mysql we need connector 

import mysql.connector
data=mysql.connector.connect(host="localhost",user="root",password="171119@aditya")
print(data)

mycursor=data.cursor()

#mycursor.execute("create database demo")

mycursor.execute("show databases")

for x in mycursor:
    print(x)