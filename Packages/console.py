"""Console"""
# -*- coding: utf-8 -*-
import os
import Packages.api_operations as ao
import Packages.loading as load
import time


def presentation():
    """Presentation"""
    display("*", 50, 3)
    print("********** BIENVENUE SUR PUREBERRE app ***********")
    display("*", 50, 3)
    print("*"*35+" by Stephen A.O")
    display()


def menu(big_data):
    """Menu"""
    print("1 - Quel aliment souhaitez-vous remplacer ?")
    print("2 - Retrouver mes aliments subtitués.")
    print("x - Quitter le programme.")
    choice = get_choice()
    if choice == "x":
        print("Vous avez choisi de quitter le programme")
        quit_console()
    try:
        if choice == str(1):
            print("Vous avez choisi le menu 1")
            menu_1a(big_data)
        elif choice == str(2):
            print("Vous avez choisi le menu 2")
            menu_2a(big_data)
    except ValueError:
        print("Mauvaise saisie!!\nVous avez entré {}".format(choice,))
        display("*", 50, 5)


def menu_1a(big_data):
    """ Category"""
    display("*", 50, 5)
    while 1:
        print("Veuillez sélectionner la catégorie de votre aliment.")
        dict_category = get_categories(big_data)
        print("\nx -  menu principal")
        choice = get_choice()
        if choice == "x":
            print("Vous avez choisi le retour au menu principal")
            menu(big_data)
        try:
            if choice in str(dict_category.keys()):
                big_data["user"] = {"category": dict_category[int(choice)]}
                print("Vous avez fait le choix {} - choisi la catégorie : {}".format(choice, big_data["user"]["category"]))
                menu_1b(big_data)
        except ValueError:
            print("Mauvaise saisie!!\nVous avez entré {}".format(choice))
            display("*", 50, 5)


def menu_1b(big_data):
    """Aliment"""
    display("*", 50, 5)
    while 1:
        print("Veuillez sélectionner l'aliment de votre choix.")
        dict_aliment = get_aliments(big_data)
        print("\nx -   menu principal")
        choice = get_choice()
        if choice == "x":
            print("Vous avez choisi le retour au menu principal")
            menu(big_data)
        try:
            if int(choice):
                big_data["user"]["aliment"] = dict_aliment[int(choice)]
                print("Vous avez fait le choix {} - l'aliment {}".format(choice, big_data["user"]["aliment"]))
                menu_1c(big_data)
        except ValueError:
            print("Mauvaise saisie!!\nVous avez entré {}".format(choice))
            display("*", 50, 5)


def menu_1c(big_data):
    """Substitute"""
    substitute = get_substitute(big_data)
    display("*", 50, 5)
    display_substitute(big_data, substitute)
    while 1:
        print("\nVoulez-vous le sauvegarder ?")
        print("1 - sauvegarder ?")
        print("x - Retour au menu principal")
        choice = get_choice()
        try:
            if choice == str(0):
                print("Vous avez choisi le retour au menu principal")
                display("*", 50, 5)
                menu(big_data)
            if choice == str(1):
                print("Vous avez choisi de sauvegarder cette opération")
                menu_1d(big_data)
        except ValueError:
            print("\nMauvaise saisie!!\nVous avez entré {}".format(choice))
            display("*", 50, 5)


def menu_1d(big_data):
    """Save"""
    display("*",50, 5)
    print("l'aliment et son substitut ont été sauvegardé !")
    display("*",50, 5)
    menu(big_data)


def menu_2a(big_data):
    """Historic"""
    display("*",50, 5)
    print("Voici l'historique des aliments substitués")
    display("*", 50, 5)
    print("0 - Menu principal.")
    choice = get_choice()
    if choice == str(0):
        print("Vous avez choisi le menu 0")
        menu(big_data)
    else:
        print("\nMauvaise saisie!!\nVous avez entré {}".format(choice))


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
    for i, e in enumerate(big_data["console"]["aliments"][big_data["user"]["category"]]):
        print("{} - {}".format(i, e))
        dict_aliments[i] = e
    return dict_aliments


def get_substitute(big_data):
    """ Substitute """
    substitute = {}
    aliment = big_data["user"]
    for k in big_data["console"]["substitute"].keys():
        if k == aliment["category"]:
            substitute[k] = big_data["console"]["substitute"][k]
    return substitute


def display_aliment(big_data):
    aliment_name = big_data["user"]["aliment"]
    aliment_category = big_data["user"]["category"]
    print("En fonction de l'aliment {}".format(aliment_name))
    display("_", 50, 1)
    for aliment in big_data["console"]["aliments"][aliment_category].keys():
        if aliment == aliment_name:
            for k, v in big_data["console"]["rows"].items():
                if k == "local_category":
                    print("{} : {} ".format(v, aliment_category))
                else:
                    print("{} : {} ".format(v, big_data["console"]["aliments"][aliment_category][aliment_name][k]))
    display("_", 50, 1)


def display_substitute(big_data, substitute):
    substitute_name = ""
    substitute_category = ""
    display_aliment(big_data)
    print("\nVoici le substitut proposé :\n")
    for key in substitute.keys():
        substitute_category = key
    for value in substitute[substitute_category].keys():
        substitute_name = value
    display("_", 50, 1)
    for k, v in big_data["console"]["rows"].items():
        if k == "local_category":
            print("{} : {} ".format(v, substitute_category))
        else:
            print("{} : {} ".format(v, substitute[substitute_category][substitute_name][k]))
    display("_", 50, 1)


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
