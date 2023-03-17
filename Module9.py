#!/usr/bin/env python3

#Module8.py
#Keegan Brennan
#3/30/2021
#SQL

#import pyodbc

def main():
    conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'Trusted_Connection=yes;',
    autocommit = True)

    insertRow1SQL = "INSERT INTO COP2034.dbo.Customer VALUES ('A10001', 'Smith', 'John', '1 Elm St.,', 'Jacksonville', 'FL', '32242')"
    insertRow2SQL = "INSERT INTO COP2034.dbo.Customer VALUES ('B10002', 'Brown', 'Sally', '3 Oak St.,', 'Orlando', 'FL', '32806')"
    deleteRow1SQL = 'DELETE FROM COP2034.dbo.Customer'
    dropTableSQL = 'DROP TABLE COP2034.dbo.Customer'
    c.execute('SELECT * FROM COP2034.dbo.Customer')
    while True:
        cust = c.fetchone()
        if cust == None:
            break
        print("Customer:")
        print("\tID:    " + cust[0])
        print("\tLName  " + cust[1])
        print("\tFname  " + cust[2])
        createTableSQL = ('CREATE TABLE COP2034.dbo.Customer ('
                    'CustomerID varchar(10),'
                    'LastName varchar(255),'
                    'FirstName varchar(255),'
                    'Address varchar(255),'
                    'City varchar(127),'
                    'State varchar(2),'
                    'Zip varchar(9) );')
    if conn:
    # create the table
    c = conn.cursor()
    conn.execute(createTableSQL)
    conn.execute(insertRow1SQL)
    conn.execute(insertRow2SQL)
    conn.execute('CREATE DATABASE COP2034')
    conn.execute('ALTER DATABASE COP2034 SET AUTO_CLOSE OFF')
    conn.execute(deleteRow1SQL)
    conn.execute('DROP DATABASE COP2034')
    conn.execute(dropTableSQL)
    # close the connection
    conn.close()
    else:
    print('Could not get connection!')

    