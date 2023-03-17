#!/usr/bin/env python3

#Module12.py
#Keegan Brennan
#4/27/2021
#Matplotlib

import matplotlib as mpl
import matplotlib.pyplot as plt
import pyodbc 
import pandas as pd
import csv
import numpy as np

#Define variables
x = ''
y = ''

#Calculate fitted line
def plotfit(x, y):
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m*x + b, color='orange') 

def part1():
    
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;Trusted_Connection=yes;',autocommit= True)

    if conn:
        c = conn.cursor()
        df = pd.read_csv("PalmerPenguins-Combined.csv")
        plt.plot(df['CulmenLength_mm'], df['CulmenDepth_mm'], 'o', color='black')
        x = df.dropna().CulmenLength_mm
        y = df.dropna().CulmenDepth_mm
        m, b = np.polyfit(x, y, 1)
        plt.plot(x,m*x + b)
        plt.show()
        return x,y
        conn.close()
    else:
        print("Sorry, the connection couldn't be established.")

def part2():
    
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;Trusted_Connection=yes;',autocommit= True)

    if conn:
        c = conn.cursor()
        df = pd.read_csv("PalmerPenguins-Combined.csv")
        plt.plot(df['CulmenLength_mm'], df['CulmenDepth_mm'], 'o', color='black')
        #Chinstrap fitted line
        chinstrap = df[df.Species == 'Chinstrap']
        plt.plot(chinstrap.CulmenLength_mm, chinstrap.CulmenDepth_mm,
                'o', color='red', label='Chinstrap')
        plotfit(chinstrap.dropna().CulmenLength_mm,
                chinstrap.dropna().CulmenDepth_mm)
        #Adelie fitted line
        adelie = df[df.Species == 'Adelie']
        plt.plot(adelie.CulmenLength_mm, adelie.CulmenDepth_mm,
                'x', color='green', label='Adelie')
        plotfit(adelie.dropna().CulmenLength_mm,
                adelie.dropna().CulmenDepth_mm)
        #Gentoo fitted line
        gentoo = df[df.Species == 'Gentoo']
        plt.plot(gentoo.CulmenLength_mm, gentoo.CulmenDepth_mm,
                '*', color='blue', label='Gentoo')
        plotfit(gentoo.dropna().CulmenLength_mm,
                gentoo.dropna().CulmenDepth_mm)
        plt.show()
        return x,y
        conn.close()
    else:
        print("Sorry, the connection couldn't be established.")       

part1()
part2()

