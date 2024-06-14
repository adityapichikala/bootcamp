'''
create database futurense;

use futurense;
'''

'''
create table student(

sid int primary key auto_increment,

sname varchar(50) not null,

phonenumber int not null,

age int(2) not null,

gender enum("Male","Female","Others"),

email varchar(50) unique,

address varchar(100) not null

);

'''

'''
create table teacher(

tid int primary key auto_increment,

tname varchar(50) not null,

phonenumber int not null,

age int(2) not null,

gender enum("Male","Female","Others"),

email varchar(50) unique,

address varchar(100) not null

);

'''