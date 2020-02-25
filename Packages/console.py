"""Console"""
# -*- coding: utf-8 -*-
import os
import Packages.api_operations as ao
import Packages.loading as load
import time


def presentation():
    """Presentation"""
    display(" ", 50, 3)
    display("~", 50, 3)
    print("~~~~~~~~~~ BIENVENUE SUR PUREBERRE app ~~~~~~~~~~")
    display("~", 50, 3)
    print("~"*35+" by Stephen A.O")
    display("~", 50)
    display(" ", 50, 3)
    display()


def menu(big_data):
    """Menu"""
    while 1:
        print("1 - Quel aliment souhaitez-vous remplacer.")
        print("2 - Retrouver mes aliments subtitués.")
        print("x - Quitter le programme.")
        display("*", 50)
        choice = get_choice()
        try:
            if choice == "x":
                print("Vous avez choisi de quitter le programme")
                quit_console()
            if choice == str(1):
                print("Vous avez choisi le menu 1")
                menu_1a(big_data)
            elif choice == str(2):
                print("Vous avez choisi le menu 2")
                menu_2a(big_data)
        except ValueError or KeyError:
            print("Mauvaise saisie!!\nVous avez entré {}".format(choice,))
            display("*", 50, 5)


def menu_1a(big_data):
    """ Category"""
    display("*", 50, 5)
    while 1:
        print("Sélectionnez la catégorie.")
        display("*", 50)
        dict_category = get_categories(big_data)
        print("\nx -  menu principal")
        display("*", 50)
        choice = get_choice()
        try:
            if choice == "x":
                print("Vous avez choisi le retour au menu principal")
                interface(big_data)
            if choice in str(dict_category.keys()):
                big_data["user"] = {"category": dict_category[int(choice)]}
                print("Vous avez fait le choix {}, la catégorie : {}".format(choice, big_data["user"]["category"]))
                menu_1b(big_data)
        except ValueError or KeyError:
            print("Mauvaise saisie!!\nVous avez entré {}".format(choice))
            display("*", 50, 5)


def menu_1b(big_data):
    """Aliment"""
    display("*", 50, 5)
    while 1:
        print("Sélectionnez l'aliment.")
        display("*", 50)
        dict_aliment = get_aliments(big_data)
        print("\nx -   menu principal")
        display("*", 50)
        choice = get_choice()
        try:
            if choice == "x":
                print("Vous avez choisi le retour au menu principal")
                interface(big_data)
            if int(choice) <= len(dict_aliment):
                big_data["user"]["aliment"] = dict_aliment[int(choice)]
                print("Vous avez fait le choix {} - l'aliment {}".format(choice, big_data["user"]["aliment"]))
                display_aliment(big_data)
                menu_1c(big_data)
        except Exception as e:
            print(e)
            print("Mauvaise saisie!!\nVous avez entré {}".format(choice))
            display("*", 50, 5)


def menu_1c(big_data):
    """Substitute"""
    while 1:
        substitute = get_substitute(big_data)
        aliment = big_data["user"]
        display("*", 50, 5)
        display_substitute(big_data, substitute)
        display("*", 50, 2)
        print("Voulez-vous sauvegarder cet échange ?")
        display("*", 50)
        print("1 - sauvegarder ?")
        print("x - Retour au menu principal")
        display("*", 50)
        choice = get_choice()
        try:
            if choice == "x":
                print("Vous avez choisi le retour au menu principal")
                display("*", 50, 5)
                interface(big_data)
            if choice == str(1):
                print("Vous avez choisi de sauvegarder cette opération")
                save_data(big_data, aliment, substitute)
        except ValueError or KeyError:
            print("\nMauvaise saisie!!\nVous avez entré {}".format(choice))
            display("*", 50, 5)


def menu_1c0(big_data):
    """Historic"""
    display("*",50, 5)
    while 1:
        display("~", 50)
        print("\n~~~~~ Aucun substitut ne peut être proposé !! ~~~~~~~~~~~~")
        print("\n" + "~~ L'aliment sélectionné possède le meilleur nutriscore ~~")
        display("~", 50)
        print("\nPour recommencer votre sélection,\nretournez au menu principale.\n")
        print("0 - Menu principal.")
        display("*", 50)
        choice = get_choice()
        try:
            if choice == str(0):
                print("Vous avez choisi le menu 0")
                interface(big_data)
            else:
                print("\nMauvaise saisie!!\nVous avez entré {}".format(choice))
        except ValueError:
            print("\nMauvaise saisie!!\nVous avez entré {}".format(choice))
            display("*", 50, 5)


def menu_2a(big_data):
    """Historic"""
    display("*",50, 5)
    while 1:
        print("Historique des aliments substitués")
        display("*", 50)
        display_historic(big_data)
        print("0 - Menu principal.")
        display("*", 50)
        choice = get_choice()
        try:
            if choice == str(0):
                print("Vous avez choisi le menu 0")
                interface(big_data)
            else:
                print("\nMauvaise saisie!!\nVous avez entré {}".format(choice))
        except ValueError:
            print("\nMauvaise saisie!!\nVous avez entré {}".format(choice))
            display("*", 50, 5)


def quit_console():
    print("Fermeture de la console en cours ...")
    time.sleep(3)
    exit()


def display(sign="*", number=50, lines=1):
    for i in range(0, lines):
        print("{}".format(sign)*number)


def get_choice():
    """Text entry"""
    text = input("Que voulez-vous faire : ")
    display("*",50, 5)
    return text


def get_categories(big_data):
    """Categories"""
    dict_category = {}
    for i, e in enumerate(big_data["rcvd"]["local_category"]):
        print("{} - {}".format(i, e))
        dict_category[i] = e
    return dict_category


def get_aliments(big_data):
    dict_aliments = {}
    user_category = big_data["user"]["category"]
    for i, e in enumerate(big_data["console"]["aliments"][user_category]):
        title = big_data["console"]["aliments"][user_category][e]["product_name"]
        print("{} : {}".format(i, title))
        dict_aliments[i] = e
    return dict_aliments


def get_substitute(big_data):
    """ Substitute """
    substitute = {}
    aliment = big_data["user"]
    for k in big_data["console"]["substitute"].keys():
        if k == aliment["category"]:
            substitute[k] = big_data["console"]["substitute"][k]
            check_score(substitute[k], big_data)
            break
    return substitute


def check_score(substitute, big_data):
    aliment = big_data["user"]
    for key, value in big_data["console"]["aliments"].items():
        if key == aliment["category"]:
            for k, v in value.items():
                if k == aliment["aliment"]:
                    aliment_info = {k: v}
                    break
    for key, value in aliment_info.items():
        for k, v in substitute.items():
            sub = v["nutriscore_grade"]
            ali = aliment_info[key]["nutriscore_grade"]
            if sub >= ali:

                menu_1c0(big_data)




def save_data(big_data, aliment, substitute):
    """Save"""
    big_data["save"] = {"aliment": aliment["aliment"]}
    for k, v in substitute.items():
        for ke in v.keys():
            big_data["save"]["substitute"] = ke
    load.fill_table_historic(big_data)
    display("*", 50, 5)
    print("l'aliment et son substitut ont été sauvegardé !")
    display("*", 50, 5)
    interface(big_data)


def off_display_aliment(big_data):
    aliment = big_data["user"]
    for key, value in big_data["console"]["aliments"].items():
        if key == aliment["category"]:
            for k, v in value.items():
                if k == aliment["aliment"]:
                    for ke, va in v.items():
                        print("====> {} : {}".format(ke, va))
                    break


def display_aliment(big_data):
    all_aliments = big_data["console"]["aliments"].items()
    aliment = big_data["user"]
    category = aliment["category"]
    aliment_name = aliment["aliment"]
    for key, value in all_aliments:
        if key == category:
            for k, v in value.items():
                if k == aliment_name:
                    for ke, va in v.items():
                        row = big_data["console"]["rows"][ke]
                        print("====> {} : {}".format(row, va))
                    break


def display_all_aliments(big_data):
    aliment_name = big_data["user"]["aliment"]
    aliment_category = big_data["user"]["category"]
    display("~", 50, 2)
    print("En fonction de l'aliment {}".format(aliment_name))
    for aliment in big_data["console"]["aliments"][aliment_category].keys():
        if aliment == aliment_name:
            for k, v in big_data["console"]["rows"].items():
                if k == "local_category":
                    print("====> {} : {} ".format(v, aliment_category))
                else:
                    print("====> {} : {} ".format(v, big_data["console"]["aliments"][aliment_category][aliment_name][k]))


def display_substitute(big_data, substitute):
    substitute_name = ""
    substitute_category = ""
    display_all_aliments(big_data)
    print("\nVoici le substitut proposé :")
    for key in substitute.keys():
        substitute_category = key
    for value in substitute[substitute_category].keys():
        substitute_name = value
    for k, v in big_data["console"]["rows"].items():
        if k == "local_category":
            print("====> {} : {} ".format(v, substitute_category))
        else:
            print("====> {} : {} ".format(v, substitute[substitute_category][substitute_name][k]))
    display("~", 50, 2)




def display_historic(big_data):
    big_data = load.read_table_historic(big_data)
    if len(big_data["console"]["historic"]["graphic"]) == 0:
        display("~", 50)
        print(" "*5+"~~~~~ L'historique est vide ~~~~~")
        display("~", 50)
        return 0
    for k, v in big_data["console"]["historic"]["graphic"].items():
        print("REMPLACEMENT {}".format(k))
        display("*", 50)
        for ke, va in v.items():
            print("{}".format(ke))
            i = 0
            for element in va[0]:
                row = big_data["console"]["historic"]["read_rows"][i]
                print("====> {} : {} ".format(row, element))
                i += 1
            print("\n")
        display("*", 50)


def interface(big_data):
    """Interface"""
    presentation()
    while 1:
        menu(big_data)


def start_program():
    display("*",50, 5)
    print("interface running...")
    display("*",50, 5)
    big_data = load.initialization()
    interface(big_data)


if __name__ == "__main__":
    start_program()
