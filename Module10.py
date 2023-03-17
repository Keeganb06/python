#!/usr/bin/env python3

#Module10.py
#Keegan Brennan
#4/12/2021
#Numpy

import sys
import pyodbc
import numpy as np

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
'SERVER=localhost;'
'Trusted_Connection=yes;',  # use Windows Authentication
autocommit= True)

if conn:
    c = conn.cursor()

#SQL query and assign 0 to NULL values
c.execute('SELECT ISNULL (culmen_length_mm,0) as bill_len, ISNULL (culmen_depth_mm,0) as bill_depth FROM palmer_penguins.dbo.penguin')

arr = [0,2]

while True:
    cust= c.fetchone()
    if cust== None:
        break
    arr.append([cust[0], cust[1]])
    

conn.close()

print("Array: ", arr)

npArr = np.array(arr, dtype = object)

#print array description
print(npArr.flags)
print(npArr.size)

#print summary statistics of array
print("Mean: ", npArr.mean)
print("Min: ", npArr.min)
print("Max: ", npArr.max)

#print values that are not a number
print(np.isnan(npArr))

