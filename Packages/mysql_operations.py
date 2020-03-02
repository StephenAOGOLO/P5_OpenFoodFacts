"""
Welcome to the MYSQL Operations module, 'mysql_operations.py'.
This module is especially composed of one class 'Mysql'.
Nine methods to create, fill and read MYSQL database and tables.
"""
# -*- coding: utf-8 -*-
import mysql.connector as mc
import logging as lg
lg.basicConfig(level=lg.WARNING)


class Mysql:
    """Mysql class creates an instance which handling
     many MYSQL operations."""

    def __init__(self, usr, psw, db="", hst="localhost"):
        """
        Init constructor has six attributes:
        self.user : MYSQL username
        self.password : MYSQL user password
        self.host : MYSQL server location
        self.db : MYSQL database name
        self.cnx : MYSQL session
        self.cursor : MYSQL session pointer
        """
        self.user = usr
        self.password = psw
        self.host = hst
        self.db = db
        self.cnx = self.connection()
        self.cursor = self.cursor_connection()

    def connection(self):
        """
        'connection' method establishes an opened session
        to the MYSQL server.
        :return:
        """
        cnx = mc.connect(
            host=self.host,
            user=self.user,
            passwd=self.password,
            database=self.db
        )
        lg.info(cnx)
        return cnx

    def cursor_connection(self):
        """
        'cursor_connection' method sets a pointer
        used to execute MYSQL instruction in the session.
        :return:
        """
        my_cursor = self.cnx.cursor()
        return my_cursor

    def create_db(self, db="db_purebeurre"):
        """
        'create_db' method try to create a table
        into a database given as parameter.
        :param db:
        :return:
        """
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
        """
        'select_from' method gets data
         from a table and a row, both given as parameter.
         It returns a list of tuples.
        :param row:
        :param tb:
        :return:
        """
        formula = "SELECT {} FROM {}".format(row, tb)
        self.cursor.execute(formula)
        results = self.cursor.fetchall()
        for result in results:
            lg.info(result)
        return results

    def select_from_where(self, row, tb, w_clause):
        """
        'select_from_where' method gets data
         from a table, a row and a criteria all of them given as parameter.
         It returns a list of tuples.
        :param row:
        :param tb:
        :param w_clause:
        :return:
        """
        formula = "SELECT {} FROM {} WHERE {}".format(row, tb, w_clause)
        self.cursor.execute(formula)
        results = self.cursor.fetchall()
        for result in results:
            lg.info(result)
        return results

    def close_connection(self):
        """
        'close_connection' method close the running MYSQL session.
        :return:
        """
        return self.cnx.close

    def insert_data(self, tb, rows, values):
        """
        'insert_data' method inserts data
         into a table.
        :param tb:
        :param rows:
        :param values:
        :return:
        """
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

    def executing(self, cmd):
        """
        'executing' method runs the command
        stored into the MYSQL session pointer.
        :param cmd:
        :return:
        """
        status = True
        try:
            self.cursor.execute(cmd)
            self.cnx.commit()
        except Exception as e:
            lg.warning(e)
            status = e
        return status


