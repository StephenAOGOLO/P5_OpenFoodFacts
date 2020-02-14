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


def off_initialization():
    """
    So this function is ran to concentrate these parameters first and return dict ready to use.
    """
    os.system(".\\Packages\\root_link.bat")
    root_status = False
    while 1:
        process_report = find_process("mysql.exe")
        print(process_report)
        if process_report[1]:
            print("vrai")
        else:
            print("faux")
            root_status = True
            break
    return root_status


def initialization():
    create_db_purebeurre()
    #big_data = ao.load_api_data()
    #fill_table_category(big_data)
    #fill_table_aliment(big_data)


def create_db_purebeurre():
    session = mo.Mysql("stephen", "stephen")
    session.create_db()
    session = mo.Mysql("stephen", "stephen", "db_purebeurre")
    contenu = open_sql_file("test.sql")
    contenu = "".join(contenu)
    contenu = contenu.replace("\n","")
    contenu = contenu.split(";")
    dict_tables = {"category":contenu[0],"aliment":contenu[1],"historic":contenu[2]}
    create_tables(dict_tables)


def create_tables(tables_data):
    session = mo.Mysql("stephen", "stephen", "db_purebeurre")
    for table, data in tables_data.items():
        session.executing(data)
    return True


def create_table_category():
    pass


def create_table_aliment():
    pass


def create_table_historic():
    pass

def fill_table_category(dico):
    ## TABLE CATEGORY
    session = mo.Mysql("stephen", "stephen")
    #dico = ao.load_api_data()
    for i, category in enumerate(dico["rcvd"]["local_category"]):
        pure_value = "('{}', '{}')".format(i+1, category)
        session.insert_data("category", "(id, name)", pure_value)


def fill_table_aliment(dico):

    # TABLE ALIMENT
    session = mo.Mysql("stephen", "stephen")
    #dico = ao.load_api_data()
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


def find_process(the_process="le_program_executable.exe"):
    dico_processus = {}
    status = False
    for indice, process in enumerate(psutil.process_iter()):
        if process.name() == the_process:
            lg.info("Voici le/les processus %s en cours d'execution", the_process)
            lg.info("%s", process)
            dico_processus[str(indice)] = {}
            dico_processus[str(indice)]["nom"] = process.name()
            dico_processus[str(indice)]["pid"] = process.pid
            dico_processus[str(indice)]["complete_info"] = process
            status = True
        else:
            lg.info("le/les processus %s est/sont introuvable(s)", the_process)
            pass
    return dico_processus, status


def open_sql_file(path_fichier):
    """ Fonction d'ouverture d'un fichier
                        et
        sauvegrade du contenu en mémoire

    :param path_fichier:
    :return liste_fichier: """

    with open(path_fichier,"rt") as fichier:
        liste_fichier = fichier.readlines()
    print("=" * 150)
    print("\nVoici le contenu du fichier : {}\n".format(path_fichier))
    for indice, ligne in enumerate(liste_fichier):
        print("ligne {} : {}".format(indice, ligne))
    print("=" * 150)
    print("\nFin de fichier\n")
    print("=" * 150)
    return liste_fichier

if __name__ == "__main__":
    initialization()
    #contenu = open_sql_file("test.sql")
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





