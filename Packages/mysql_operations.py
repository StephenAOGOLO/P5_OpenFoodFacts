# -*- coding: utf-8 -*-
import mysql.connector as mc
import logging as lg

lg.basicConfig(level=lg.WARNING)


class Mysql:

    def __init__(self, usr, psw, db="", hst="127.0.0.1"):
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

    def create_db(self, db="db_purebeurre"):
        status = False
        try:
            cmd = "CREATE DATABASE "
            self.cursor.execute(cmd+db)
            self.cnx.commit()
        except mc.errors.DatabaseError as e:
            lg.info(e)
            print("Il existe déjà une base de données !!")
            status = True
        return status

    def create_tb(self, tb):
        status = False
        try:
            cmd = "CREATE TABLE "
            self.cursor.execute(cmd+tb)
            self.cnx.commit()
        except mc.errors.DatabaseError as e:
            lg.info(e)
            print("Tables already created")
            status = True
        return status

    def drop_db(self, db):
        cmd = "DROP DATABASE "
        self.cursor.execute(cmd+db)

    def drop_tb(self, tb):
        cmd = "DROP TABLE "
        self.cursor.execute(cmd+tb)

    def select_from(self, row, tb):
        formula = "SELECT {} FROM {}".format(row, tb)
        self.cursor.execute(formula)
        results = self.cursor.fetchall()
        for result in results:
            lg.info(result)
        return results

    def select_from_where(self, row, tb, w_clause):
        formula = "SELECT {} FROM {} WHERE {}".format(row, tb, w_clause)
        self.cursor.execute(formula)
        results = self.cursor.fetchall()
        for result in results:
            lg.info(result)
        return results

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
        status = False
        try:
            formula = "INSERT INTO {} {} VALUES {}".format(tb, rows, values)
            self.cursor.execute(formula)
            self.cnx.commit()
        except mc.errors.IntegrityError as e:
            lg.info(e)
            print("Entry already done")
            status = True
        return status

    def display_data(self):
        for e in self.cursor:
            print(e)
        print("*" * 50)

    def executing(self, cmd):
        status = False
        try:
            self.cursor.execute(cmd)
            self.cnx.commit()
        except mc.errors as e:
            lg.info(e)
            print("Tables already created")
            status = True
        return status

    def executing_2(self, cmd, arg):
        self.cursor.execute(cmd, arg)

