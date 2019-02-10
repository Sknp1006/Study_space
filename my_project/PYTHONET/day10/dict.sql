create database dict default charset=utf8;
use dict
create table user(
    id int primary key auto_increment,
    name varchar(32) not null,
    passwd varchar(16) default '000000'
)default charset=utf8;

create table hist(
    id int primary key auto_increment,
    name varchar(32) not null,
    word varchar(32) not null,
    time VARCHAR(64)
)

create table words(
    id int PRIMARY KEY auto_increment,
    word varchar(32),     
    interpret text 
)default charset=utf8;