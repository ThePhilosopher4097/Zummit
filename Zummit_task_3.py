import mysql.connector
from mysql.connector.errors import _ERROR_EXCEPTIONS, custom_error_exception

cnx = mysql.connector.connect(host = "remotemysql.com", user="q0k6st2xWR",password="7DspOUbqHb", database="q0k6st2xWR")
cursor = cnx.cursor(buffered=True)

def createTable() :
    query = ("CREATE TABLE PRODUCT (pid int(10) primary key, pname varchar(40) not null, pdescription varchar(100) not null, price double(10,2), pimage BLOB, pdate date not null);")
    cursor.execute(query)
    query = ("CREATE TABLE CUSTOMER (cid int(10) primary key, cname varchar(40) not null, phone int(10) not null, email varchar(50) not null, address varchar(100) not null, city varchar(40));")
    cursor.execute(query)
    query = ("CREATE TABLE ORDER_Table (oid int(10) primary key, odate date NOT NULL, quantity int(10) not null, billing int(10), pid int(10) not null, cid int(10) not null, FOREIGN KEY(pid) REFERENCES PRODUCT(pid), FOREIGN KEY(cid) REFERENCES CUSTOMER(cid))")
    cursor.execute(query)

#createTable()
# mysql