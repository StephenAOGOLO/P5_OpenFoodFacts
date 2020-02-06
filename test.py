"""
Welcome to the main program 'test.py'.
When it starts the program process is following the steps below:
- The initialization
- The provided parameters
- The player management
- The endgame:
"""
# -*- coding: utf-8 -*-
import mysql.connector as mc
import Packages.loading as ld
import Packages.mysql_operations as mo
import requests
import json
import time
import logging as lg
lg.basicConfig(level=lg.WARNING)


def close_connection():
    cnx.close


def main_off():

    cnx = mc.connect(
        host="127.0.0.1",
        user="stephen",
        passwd="stephen"
    )
    print(cnx)
    #mycursor = cnx.cursor()
    ##mycursor.execute("GRANT ALL PRIVILEGES ON db_purebeurre.* TO 'stephen'@'localhost';")
    #mycursor.execute("CREATE DATABASE db_purebeurre")
    #mycursor.execute("SHOW DATABASES")
    #for db in mycursor:
    #    print(db)


def main_of_reset():
    ld.initialization()


def open_json_file(file):
    with open(file) as f:
        data = json.load(f)
    return data


def load_api_data():
    dict_data = {}
    list_c = ["product_name", "categories", "brands", "nutriscore_grade", "stores", "purchase_places", "url"]
    dict_data["sent"] = {}
    dict_data["rcvd"] = {}
    dict_data["sent"]["urls"] = open_json_file(".\\Packages\\urls.json")
    for url_name, url in dict_data["sent"]["urls"].items():
        response = requests.get(url)
        dict_data["rcvd"][url_name] = response.json()
    dict_data["rcvd"]["aliments"] = {}

    for url_name, url in dict_data["sent"]["urls"].items():
        dict_data["rcvd"]["aliments"][url_name] = {}
        for i in range(0, 30):
            dict_data["rcvd"]["aliments"][url_name][str(i)] = {}
            for element in list_c:
                if element in dict_data["rcvd"][url_name]["products"][i]:
                    dict_data["rcvd"]["aliments"][url_name][str(i)][element] = dict_data["rcvd"][url_name]["products"][i][element]

    return dict_data


if __name__ == "__main__":

    dico = load_api_data()
    for i in range(0, 30):
        print("*"*10)
        for k, v in dico["rcvd"]["aliments"]["steack"][str(i)].items():
            print("{} : {}".format(k, v))
