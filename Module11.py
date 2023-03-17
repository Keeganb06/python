#!/usr/bin/env python3

#Module11.py
#Keegan Brennan
#4/20/2021
#Pandas

import sys
import pyodbc
import pandas as pd
import numpy as np


def main():
    
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;Trusted_Connection=yes;',autocommit= True)

    if conn:
        c = conn.cursor()
        df = pd.read_sql_query('SELECT * FROM palmer_penguins.dbo.penguin', conn)
        #display the data types
        print(df.dtypes)
        #summary statistics for the columns
        print(df.describe(include = "all",datetime_is_numeric = "true"))
        #calculate correlatio between 
        print("Correlation = ",df['culmen_length_mm'].corr(df['culmen_depth_mm']))
        
        #filter rows for each species using  the boolean expression
        df_Adelie = df[df.species.eq('Adelie')]
        print("Correlation for Adelie is ",df_Adelie['culmen_length_mm'].corr(df_Adelie['culmen_depth_mm']))
        df_Chinstrap = df[df.species.eq('Chinstrap')]
        print("Coreelation for Chinstrap is ",df_Chinstrap['culmen_length_mm'].corr(df_Chinstrap['culmen_depth_mm']))
        df_Gentoo = df[df.species.eq('Gentoo')]
        print("Correlation for Gentoo is ",df_Gentoo['culmen_length_mm'].corr(df_Gentoo['culmen_depth_mm']))
        conn.close()
    else:
        print("Sorry, the connection couldn't be established.")

main()
