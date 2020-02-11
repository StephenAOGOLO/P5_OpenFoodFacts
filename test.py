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
    list_c = ["product_name", "brands", "nutriscore_grade", "stores", "purchase_places", "url"]
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
    dict_data = all_rows(dict_data)
    dict_data = all_categories(dict_data)
    dict_data = prepare_sql_values(dict_data)
    return dict_data


def all_categories(all_data):
    all_data["rcvd"]["local_category"]=[]
    for key in all_data["rcvd"]["aliments"].keys():
        all_data["rcvd"]["local_category"].append(key)
    return all_data


def all_rows(all_data):

    all_data["rcvd"]["rows"] = ["product_name",
                                "local_category",
                                "brands",
                                "nutriscore_grade",
                                "stores",
                                "purchase_places",
                                "url"
                                ]
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
    for category in list_categories:
        for i in range(0, 20):
            for row in all_data["rcvd"]["rows"]:
                try:
                    the_row = all_data["rcvd"]["sql_values"][category][category+"_"+str(i)][row]
                    the_row = str(the_row).replace(","," ou ")
                    the_row = the_row.replace("'","-")
                    all_data["rcvd"]["sql_values"][category][category + "_" + str(i)][row] = the_row
                except Exception as e:
                    lg.info("erreur sur part - ", e)
    for k, v in all_data["rcvd"]["sql_values"]["beurre"].items():
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


def fill_table_category():
    ## TABLE CATEGORY
    session = mo.Mysql("stephen", "stephen")
    dico = load_api_data()
    for i, category in enumerate(dico["rcvd"]["local_category"]):
        pure_value = "('{}', '{}')".format(i+1, category)
        session.insert_data("category", "(id, name)", pure_value)


def fill_table_aliment():

    # TABLE ALIMENT
    session = mo.Mysql("stephen", "stephen")
    dico = load_api_data()
    for category in dico["rcvd"]["local_category"]:
        for i in range(0, 20):
            raw_data = ""
            dico["rcvd"]["sql_values"][category + "_" + str(i)] = {}
            dico["rcvd"]["sql_values"][category + "_" + str(i)]["pure_data"] = []
            dico["rcvd"]["sql_values"][category + "_" + str(i)]["raw_data"] = ""
            i_rows = 0
            for k, v in dico["rcvd"]["sql_values"][category][category+"_"+str(i)].items():
                dico["rcvd"]["sql_values"][category + "_" + str(i)]["pure_data"].append(v)
                if i_rows == 0:
                    raw_data += v
                else:
                    raw_data += ", " + v
                i_rows += 1
            dico["rcvd"]["sql_values"][category + "_" + str(i)]["raw_data"] = raw_data
            raw_data = ""
    for i in range(0, 20):
        for category in dico["rcvd"]["local_category"]:
            value = dico["rcvd"]["sql_values"][category + "_" + str(i)]["raw_data"]
            value += ","+category
            value += "," + category + "_" + str(i)
            value = value.replace(",", "' , '")
            pure_value = "('{}')".format(value)
            session.insert_data("aliment", "(product_name, brands, nutriscore_grade, stores, purchase_places, url, local_category, local_name)", pure_value)


def create_products(all_data):

    pass


if __name__ == "__main__":
    fill_table_category()
    fill_table_aliment()
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