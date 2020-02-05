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
import time


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


def creation_fichier(path_fichier="./",name_fichier="fichier_genere_par_python" ,extension="txt", contenu = "vide"):

    now = time.localtime()
    when_happens = "{}-{}-{}_{}-{}-{}".format(now[0], now[1], now[2], now[3], now[4], now[5])
    creation_time = "_"+when_happens
    print("=" * 150)
    new_file = open(path_fichier+"//"+name_fichier+creation_time+"."+extension, "wt")
    for ligne in contenu:
        new_file.write(ligne)
    new_file.close
    print("le fichier '{}.{}' est prêt".format(name_fichier,extension))


def load_api_data():
    list_c = ["product_name", "generic_name", "categories", "brands", "nutriscore_grade", "stores", "purchase_places", "url"]
    url = "https://world.openpetfoodfacts.org/api/v0/product/20106836.json"
    #url = "https://fr-fr.openfoodfacts.org/categories.json"
    response = requests.get(url)
    json_response = response.json()
    print(type(json_response))
    #print(json_response)
    str_r_p = str(json_response)
    for key, value in json_response.items():
        print("{}===>{}".format(key, value))
        if type(value) is dict:
            for k, v in value.items():
                print("        {}===>{}".format(k, v))
        #if type(value) == type(json_response):
                if k in list_c:
                    print(k)
            #for value_k, value_v in value.items():
            #    print("   "+value_k, value_v)
            #    if type(value_v) == type(json_response):
            #        for value_k2, value_v2 in value_v.items():
            #            print("      "+value_k2, value_v2)
    creation_fichier("./Packages/Results/","results","txt", str_r_p)


if __name__ == "__main__":

    load_api_data()






