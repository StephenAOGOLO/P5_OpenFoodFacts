# -*- coding: utf-8 -*-
import mysql.connector as mc
import logging as lg

lg.basicConfig(level=lg.WARNING)


class Mysql:

    def __init__(self, usr, psw, hst="127.0.0.1"):
        self.user = usr
        self.password = psw
        self.host = hst
        self.cnx = self.connection()
        self.cursor = self.cursor_connection()

    def connection(self):
        cnx = mc.connect(
            host=self.host,
            user=self.user,
            passwd=self.password
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
        cmd = "SHOW TABLE "
        self.cursor.execute(cmd+tb)

    def show_db(self):
        cmd = "SHOW DATABASES "
        self.cursor.execute(cmd)

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

    def executing(self, cmd):
        self.cursor.execute(cmd)

    def executing_2(self, cmd, arg):
        self.cursor.execute(cmd, arg)
