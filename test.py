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
    url = "https://fr.openfoodfacts.org/cgi/search.pl?search_terms=ketchup&search_simple=1&action=process&json=1"
    response = requests.get(url)
    dict_response = response.json()
    for element in list_c:
        for i in range(0,20):
            if element in dict_response["products"][i]:
                print("{} ===> {}".format(element, dict_response["products"][i][element]))


if __name__ == "__main__":

    load_api_data()






