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
import Packages.aliment as al
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
        for i in range(0, 20):
            dict_data["rcvd"]["aliments"][url_name][str(i)] = {}
            for element in list_c:
                if element in dict_data["rcvd"][url_name]["products"][i]:
                    dict_data["rcvd"]["aliments"][url_name][str(i)][element] = dict_data["rcvd"][url_name]["products"][i][element]
                else:
                    dict_data["rcvd"]["aliments"][url_name][str(i)][element] = "NOT_PROVIDED"

    dict_data = prepare_sql_values(dict_data)
    dict_data = all_categories(dict_data)
    return dict_data


def all_categories(all_data):
    all_data["rcvd"]["categories"]=[]
    for key in all_data["rcvd"]["aliments"].keys():
        all_data["rcvd"]["categories"].append(key)
    return all_data


def prepare_sql_values(all_data):
    list_categories = []
    all_data["rcvd"]["sql_values"] = {}
    for key in all_data["rcvd"]["aliments"].keys():
        all_data["rcvd"]["sql_values"][key] = {}
        list_categories.append(key)
    for category in list_categories:
        for i in range(0, 20):
            all_data["rcvd"]["sql_values"][category][category+"_"+str(i)] = all_data["rcvd"]["aliments"][category][str(i)]
    for k, v in all_data["rcvd"]["sql_values"]["beurre"].items  ():
        lg.info("{} -> {}".format(k, v))
    return all_data


def display_results(all_data):

    for i in range(0, 20):
        print("*"*10)
        for k, v in all_data["rcvd"]["sql_values"]["beurre"][str(i)].items():
            print("{} : {}".format(k, v))
    print("-" * 20)


def display_sorted_results(all_data):
    list_keys = []
    for key in all_data["rcvd"]["aliments"].keys():
        list_keys.append(key)
    for i in range(0,20):
        print("*"*10)
        for key in list_keys:
            sorted_data = all_data["rcvd"]["aliments"][key][str(i)].values()
            print("{} : {}".format(key, sorted_data))
    print("-" * 20)


def create_products(all_data):

    pass


if __name__ == "__main__":
    # TABLE CATEGORY
    session = mo.Mysql("stephen", "stephen")
    dico = load_api_data()
    for i, category in enumerate(dico["rcvd"]["categories"]):
        pure_value = "('{}', '{}')".format(i+1, category)
        session.insert_data("category", "(id, name)", pure_value)

    # TABLE ALIMENT
    #session = mo.Mysql("stephen", "stephen")
    #dico = load_api_data()
    #list_values = []
    #for category in dico["rcvd"]["categories"]:
    #    list_values.append()
    #    #i = 0
    #    #for row, value in dico["rcvd"]["categories"][category][category+"_"+str(i)].items():
    #    #    pure_value = "('{}', '{}')".format(i+1, category)
    #    #    session.insert_data("aliment", "(product_name, categories, brands, nutriscore_grade, stores, purchase_places, url)", pure_value)





    #session = mo.Mysql("stephen", "stephen")
    #session.show_db()
    #session.show_tbs()
    #session.insert_data("category", "(id, name)", "('01', 'legumes')")

    #beurre_1 = al.Product()
    #print(beurre_1)
    #print(beurre_1.identity)

    #dico = load_api_data()
    #print(dico["rcvd"]["sql_values"]["pizza"]["pizza_0"])
    #print(dico["rcvd"]["aliments"].keys())
    #display_results(dico)
    #display_sorted_results(dico)


    #for i in range(0, 20):
    #    print("*"*10)
    #    for k, v in dico["rcvd"]["aliments"]["category_beurre"][str(i)].items():
    #        print("{} : {}".format(k, v))

    #list_keys = []
    #for key in dico["rcvd"]["aliments"].keys():
    #    if "category_" in key:
    #        list_keys.append(key)
    #for i in range(0,20):
    #    print("*"*10)
    #    for key in list_keys:
    #        print("{} : {}".format(key, dico["rcvd"]["aliments"][key][str(i)].values()))