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

    def close_connection(self):
        return self.cnx.close

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
        status = True
        try:
            self.cursor.execute(cmd)
            self.cnx.commit()
        except Exception as e:
            lg.warning(e)
            status = e
        return status


