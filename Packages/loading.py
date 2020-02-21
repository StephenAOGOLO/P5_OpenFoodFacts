"""
Welcome to the loading module, 'loading.py'.
This module is especially composed of one function.
Which is used to initialize and feeds program parameters.
"""
# -*- coding: utf-8 -*-
import configparser
import os
import time
import psutil
import logging as lg
import Packages.mysql_operations as mo
import Packages.api_operations as ao
lg.basicConfig(level=lg.WARNING)


def initialization():
    create_db_purebeurre()
    big_data = ao.load_api_data()
    session = mo.Mysql("stephen", "stephen", "db_purebeurre")
    fill_table_category(session, big_data)
    fill_table_aliment(session, big_data)
    return big_data


def update_db(status):
    while 1:
        if status:
            print("Voulez-vous conserver la base de données actuelle ?")
            print("~"*50)
            print("==> Si vous répondez 'Oui', les informations proposées dans cette application"
                  " seront peut-être pas à jour."
                  "\n==> Si vous répondez 'Non', L'historique de vos aliments substitués"
                  " et toutes les autres informations seront réinitialisés.")
            print("~"*50)
            print("\n0 - Oui\n1 - Non\n")
            choice = input("Quel est votre choix : ")
            if choice == str(0):
                maintain_db(choice)
                return status
            elif choice == str(1):
                maintain_db(choice)
                return status
            else:
                print("\nMauvaise saisie!!\nVous avez entré {}".format(choice))


def maintain_db(choice):
    if choice == str(0):
        print("La base de donnée actuelle va être utilisée !!")
    else:
        print("La base de donnée actuelle va être réinitilalisée !!")


def create_db_purebeurre():
    session = mo.Mysql("stephen", "stephen")
    status = session.create_db()
    status = update_db(status)
    session = mo.Mysql("stephen", "stephen", "db_purebeurre")
    contenu = open_sql_file(".\\Packages\\db_purebeurre_ready.sql")
    contenu = "".join(contenu)
    contenu = contenu.replace("\n", "")
    contenu = contenu.split(";")
    dict_tables = {"category": contenu[0], "aliment": contenu[1], "historic": contenu[2]}
    create_tables(dict_tables)
    return status


def drop_tables(session):
    session.executing("DROP TABLE IF EXISTS Historic")
    session.executing("DROP TABLE IF EXISTS Aliment")
    session.executing("DROP TABLE IF EXISTS Category")


def create_tables(tables_data):
    status = False
    session = mo.Mysql("stephen", "stephen", "db_purebeurre")
    drop_tables(session)
    for table, data in tables_data.items():
        status = session.executing(data)
    return status


def fill_table_category(session, dico):
    # TABLE CATEGORY
    for i, category in enumerate(dico["rcvd"]["local_category"]):
        pure_value = "('{}', '{}')".format(i+1, category)
        session.insert_data("category", "(id, name)", pure_value)


def fill_table_aliment(session, dico):

    # TABLE ALIMENT
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
            if "EMPTY" in value:
                continue
            if "NOT_PROVIDED" in value:
                continue
            else:
                value += "," + category
                value += "," + category + "_" + str(i)
                value = value.replace(",", "' , '")
                pure_value = "('{}')".format(value)
                session.insert_data("aliment", "(product_name, brands, nutriscore_grade, stores, purchase_places, url, local_category, local_name)", pure_value)


def fill_table_historic(dico):
    session = mo.Mysql("stephen", "stephen", "db_purebeurre")
    aliment = dico["save"]["aliment"]
    substitute = dico["save"]["substitute"]
    where_clause_a = "local_name = '{}' ".format(aliment)
    where_clause_s = "local_name = '{}' ".format(substitute)
    aliment_id = session.select_from_where("id", "aliment", where_clause_a)
    substitute_id = session.select_from_where("id", "aliment", where_clause_s)
    aliment_id = int(aliment_id[0][0])
    substitute_id = int(substitute_id[0][0])
    pure_value = "('{}', '{}')".format(aliment_id, substitute_id)
    session.insert_data("historic", "(aliment_id, substitute_id)", pure_value)


def read_table_historic(dico):
    session = mo.Mysql("stephen", "stephen", "db_purebeurre")
    dico["console"]["historic"] = {}
    dico["console"]["historic"]["swap_id"] = {}
    dico["console"]["historic"]["graphic"] = {}
    list_content = session.select_from("*", "Historic")
    for i, e in enumerate(list_content):
        lg.info("{} - {}".format(i, e))
        dico["console"]["historic"]["swap_id"][str(e[0])] = {"aliment_id": e[1], "substitute_id": e[2]}
    for k, v in dico["console"]["historic"]["swap_id"].items():
        where_clause_a = "id = '{}' ".format(v["aliment_id"])
        where_clause_s = "id = '{}' ".format(v["substitute_id"])
        aliment = session.select_from_where("*", "Aliment", where_clause_a)
        substitute = session.select_from_where("*", "Aliment", where_clause_s)
        dico["console"]["historic"]["graphic"][k] = {"aliment": aliment, "substitute": substitute}
        lg.info("{} - {}".format(k, v))
    return dico


def open_sql_file(path_file):
    """ This function is used to open sql file.
    It's feeding the content file in a list.

    :param path_file:
    :return list_file: """

    with open(path_file,"rt") as file:
        list_file = file.readlines()
    lg.info("=" * 150)
    lg.info("\nThere is the content file : {}\n".format(path_file))
    for i, line in enumerate(list_file):
        lg.info("ligne {} : {}".format(i, line))
    lg.info("=" * 150)
    lg.info("\nEnd of file\n")
    lg.info("=" * 150)
    return list_file


if __name__ == "__main__":
    initialization()
    #session = mo.Mysql("stephen", "stephen")
    #status = session.create_db()
    #print(status)
    #contenu = open_sql_file("db_purebeurre_ready.sql")
    #contenu = "".join(contenu)
    #contenu = contenu.replace("\n","")
    #contenu = contenu.split(";")
    #for e in contenu:
    #    print(e)
    #dico_tables = {}
    #dico_tables["category"] = contenu[0]
    #dico_tables["aliment"] = contenu[1]
    #dico_tables["historic"] = contenu[2]
    #print("\n")
    #for k, v in dico_tables.items():
    #    print(k, v)





