"""
Welcome to the main program 'main.py'.
When it starts the program process is following the steps below:
- The initialization
- The provided parameters
- The player management
- The endgame:
"""
# -*- coding: utf-8 -*-
import mysql.connector
import Packages.loading as ld


ld.initialization()
#cnx = mysql.connector.connect(
#    host="127.0.0.1",
#    user="stephen",
#    passwd="stephen"
#)
##print(cnx)
#mycursor = cnx.cursor()
##mycursor.execute("GRANT ALL PRIVILEGES ON db_purebeurre.* TO 'stephen'@'localhost';")
##mycursor.execute("CREATE DATABASE db_purebeurre")
#mycursor.execute("SHOW DATABASES")
#for db in mycursor:
#    print(db)
#cnx.close
