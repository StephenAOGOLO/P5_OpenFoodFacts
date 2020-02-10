# -*- coding: utf-8 -*-
import mysql.connector as mc
import logging as lg

lg.basicConfig(level=lg.WARNING)


class Mysql:

    def __init__(self, usr, psw, db="db_purebeurre", hst="127.0.0.1"):
        self.user = usr
        self.password = psw
        self.host = hst
        self.db = db
        self.cnx = self.connection()
        self.cursor = self.cursor_connection()

    def connection(self):
        cnx = mc.connect(
            host=self.host,
            user=self.user,
            passwd=self.password,
            database=self.db
        )
        lg.info(cnx)
        return cnx

    def cursor_connection(self):
        my_cursor = self.cnx.cursor()
        return my_cursor

    def create_db(self, db):
        cmd = "CREATE DATABASE "
        self.cursor.execute(cmd+db)

    def create_tb(self, tb):
        cmd = "CREATE TABLE "
        self.cursor.execute(cmd+tb)

    def drop_db(self, db):
        cmd = "DROP DATABASE "
        self.cursor.execute(cmd+db)

    def drop_tb(self, tb):
        cmd = "DROP TABLE "
        self.cursor.execute(cmd+tb)

    def select_tb_from_db(self, tb, db):
        cmd1 = "SELECT "
        cmd2 = "FROM "
        self.cursor.execute(cmd1+tb+cmd2+db)

    def select_all_from_db(self, db):
        cmd = "SELECT * FROM "
        self.cursor.execute(cmd+db)

    def show_tb(self, tb):
        print("*" * 50)
        cmd = "SHOW TABLE "
        self.cursor.execute(cmd+tb)
        print("There is the table :")
        self.display_data()

    def show_tbs(self):
        print("*" * 50)
        cmd = "SHOW TABLES"
        self.cursor.execute(cmd)
        print("There is the tables :")
        self.display_data()

    def show_db(self):
        print("*" * 50)
        cmd = "SHOW DATABASES "
        self.cursor.execute(cmd)
        print("There is the database(s) :")
        self.display_data()

    def show_columns(self, col):
        cmd = "SHOW COLUMNS "
        self.cursor.execute(cmd+col)

    def describe_tb(self, tb):
        cmd = "DESCRIBE "
        self.cursor.execute(cmd+tb)

    def close_connection(self):
        return self.cnx.close

    def load_sql_file(self, file):
        cmd = "SOURCE "
        self.cursor.execute(cmd+file)

    def insert_data(self, tb, rows, values):
        formula = "INSERT INTO {} {} VALUES {}".format(tb, rows, values)
        #aliment_1 = ("01", "legumes", "http://les-legumes.com")
        #aliment_1 = ("01", "legumes", "http://les-legumes.com")

        #formula = "INSERT INTO aliment (product_name, categories, brands, nutriscore_grade, stores, url)" \
        #          " VALUES (%s, %s, %s, %s, %s, %s)"
        #aliment_1 = ("carotte", "legumes", "Le vrai bio", "e", "Auchan", "http://carotte.com")

        #cmd1 = "INSERT INTO "
        #cmd2 = "VALUES "
        #cmd = cmd1+table+" "+row+" "+cmd2+value
        self.cursor.execute(formula)
        self.cnx.commit()

    def display_data(self):
        for e in self.cursor:
            print(e)
        print("*" * 50)

    def executing(self, cmd):
        self.cursor.execute(cmd)

    def executing_2(self, cmd, arg):
        self.cursor.execute(cmd, arg)

