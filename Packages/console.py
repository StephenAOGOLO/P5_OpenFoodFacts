"""
Welcome to the console module, 'console.py'.
This module is especially composed of functions.
twenty-one functions are defined to handle each menu steps of the interface.
"""
# -*- coding: utf-8 -*-
import sys
import time
import Packages.loading as load


def presentation():
    """
    'presentation' function is the first one
    which displays a message.
    It informs that the interface is now running.
    """
    display(" ", 50, 3)
    display("~", 50, 3)
    print("~~~~~~~~~~ BIENVENUE SUR PUREBERRE app ~~~~~~~~~~")
    display("~", 50, 3)
    print("~"*34+" Par Stephen A.O")
    display("~", 50)
    display(" ", 50, 3)
    display()


def menu(big_data):
    """
    This menu displays and drives toward the aliment exchange
    and the historic exchange. The customer is prompted to choose.
    :param big_data:
    """
    while 1:
        print("1 - Quel aliment souhaitez-vous remplacer.")
        print("2 - Retrouver mes aliments subtitués.")
        print("x - Quitter le programme.")
        display("*", 50)
        choice = get_choice()
        if choice == "x":
            print("Vous avez choisi de quitter le programme")
            quit_console()
        if choice == str(1):
            print("Vous avez choisi le menu 1")
            menu_1a(big_data)
        elif choice == str(2):
            print("Vous avez choisi le menu 2")
            menu_2a(big_data)
        else:
            wrong_entry(choice)


def menu_1a(big_data):
    """
    This menu displays all categories.
    The customer is prompted to choose.
    :param big_data:
    """
    display("*", 50, 5)
    while 1:
        print("Sélectionnez la catégorie.")
        display("*", 50)
        dict_category = get_categories(big_data)
        print("\nx -  Menu principal")
        display("*", 50)
        choice = get_choice()
        try:
            if choice == "x":
                print("Vous avez choisi le retour au menu principal")
                interface(big_data)
        except ValueError:
            wrong_entry(choice)
        try:
            if choice in str(dict_category.keys()):
                big_data["user"] = {"category": dict_category[int(choice)]}
                print("Vous avez fait le choix {}, la catégorie : {}"
                      .format(choice, big_data["user"]["category"]))
                menu_1b(big_data)
        except ValueError:
            wrong_entry(choice)


def menu_1b(big_data):
    """
    This menu displays all aliments from a category.
    The customer is prompted to choose.
    :param big_data:
    """
    display("*", 50, 5)
    while 1:
        print("Sélectionnez l'aliment.")
        display("*", 50)
        dict_aliment = get_aliments(big_data)
        print("\nx -   Menu principal")
        display("*", 50)
        choice = get_choice()
        try:
            if choice == "x":
                print("Vous avez choisi le retour au menu principal")
                interface(big_data)
            if int(choice) <= len(dict_aliment):
                big_data["user"]["aliment"] = dict_aliment[int(choice)]
                print("Vous avez fait le choix {} - l'aliment {}"
                      .format(choice, big_data["user"]["aliment"]))
                display_aliment(big_data)
                menu_1c(big_data)
            else:
                wrong_entry(choice)
        except ValueError:
            wrong_entry(choice)


def menu_1c(big_data):
    """
    This menu displays the choosen aliment and his substitute.
    The customer is prompted to save this exchange.
    :param big_data:
    """
    while 1:
        substitute = get_substitute(big_data)
        aliment = big_data["user"]
        display("*", 50, 5)
        display_substitute(big_data, substitute)
        display("*", 50, 2)
        print("Voulez-vous sauvegarder cet échange ?")
        display("*", 50)
        print("1 - Sauvegarder ?")
        print("x - Retour au menu principal")
        display("*", 50)
        choice = get_choice()
        if choice == "x":
            print("Vous avez choisi le retour au menu principal")
            display("*", 50, 5)
            interface(big_data)
        if choice == str(1):
            print("Vous avez choisi de sauvegarder cette opération")
            save_data(big_data, aliment, substitute)
        else:
            wrong_entry(choice)


def menu_1c0(big_data):
    """
    This menu is enable when no substitute has been found.
    The customer is prompted to go back to the main menu.
    :param big_data:
    """
    display("*", 50, 5)
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
                wrong_entry(choice)
        except ValueError:
            wrong_entry(choice)


def menu_2a(big_data):
    """
    This menu displays the historic of all exchange done before.
    The customer is prompted to go back to the main menu.
    :param big_data:
    """
    display("*", 50, 5)
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
                wrong_entry(choice)
        except ValueError:
            wrong_entry(choice)


def quit_console():
    """
    'quit_console' function is called to stop the whole process.
    """
    print("Fermeture de la console en cours ...")
    time.sleep(1)
    sys.exit()


def display(sign="*", number=50, lines=1):
    """
    'display' function displays characters.
    :param sign: the character which is displayed
    :param number: the number of character per line
    :param lines: the number of lines to display
    """
    for i in range(0, lines):
        print("{}".format(sign)*number)
    return i


def get_choice():
    """
    'get_choice' function prompt the customer to enter his choice
    by tapping on keyboard keys.
    :return:
    """
    text = input("Que voulez-vous faire : ")
    display("*", 50, 5)
    return text


def wrong_entry(choice):
    """
    'wrong_entry' function is called
    to alert customer on a keyboard wrong entry.
    """
    print("Mauvaise saisie!!\nVous avez entré {}".format(choice))
    display("*", 50, 5)


def get_categories(big_data):
    """
    'get_categories' function retrieving all aliment categories
    from the big data program.
    :param big_data:
    :return:
    """
    dict_category = {}
    for i, element in enumerate(big_data["rcvd"]["local_category"]):
        print("{} - {}".format(i, element))
        dict_category[i] = element
    return dict_category


def get_aliments(big_data):
    """
    'get_aliments' function retrieving all aliments
    from the big data program.
    :param big_data:
    :return:
    """
    dict_aliments = {}
    user_category = big_data["user"]["category"]
    for i, element in enumerate(big_data["console"]["aliments"][user_category]):
        title = big_data["console"]["aliments"][user_category][element]["product_name"]
        print("{} : {}".format(i, title))
        dict_aliments[i] = element
    return dict_aliments


def get_substitute(big_data):
    """
    'get_substitute' function retrieving all substitutes
    from the big data program.
    :param big_data:
    :return:
    """
    substitute = {}
    aliment = big_data["user"]
    for k in big_data["console"]["substitute"].keys():
        if k == aliment["category"]:
            substitute[k] = big_data["console"]["substitute"][k]
            check_score(substitute[k], big_data)
            break
    return substitute


def check_score(substitute, big_data):
    """
    'check_score' function analyses the aliment 'NUTRI-SCORE'
    to find the substitute.
    :param substitute:
    :param big_data:
    """
    aliment = big_data["user"]
    for key, value in big_data["console"]["aliments"].items():
        if key == aliment["category"]:
            for k_1, v_1 in value.items():
                if k_1 == aliment["aliment"]:
                    aliment_info = {k_1: v_1}
                    break
    for key, value in aliment_info.items():
        for k_1, v_1 in substitute.items():
            sub = v_1["nutriscore_grade"]
            ali = aliment_info[key]["nutriscore_grade"]
            if sub >= ali:
                menu_1c0(big_data)


def save_data(big_data, aliment, substitute):
    """
    'save_data' function stores the exchange into the historic.
    :param big_data:
    :param aliment:
    :param substitute:
    """
    big_data["save"] = {"aliment": aliment["aliment"]}
    for value in substitute.values():
        for k_1 in value.keys():
            big_data["save"]["substitute"] = k_1
    load.fill_table_historic(big_data)
    display("*", 50, 5)
    print("L'aliment et son substitut ont été sauvegardé !")
    display("*", 50, 5)
    interface(big_data)


def display_aliment(big_data):
    """
    'display_aliment' function is used to display all the aliments
    from one category.
    :param big_data:
    """
    all_aliments = big_data["console"]["aliments"].items()
    aliment = big_data["user"]
    category = aliment["category"]
    aliment_name = aliment["aliment"]
    for key, value in all_aliments:
        if key == category:
            for k_1, v_1 in value.items():
                if k_1 == aliment_name:
                    for k_2, v_2 in v_1.items():
                        row = big_data["console"]["rows"][k_2]
                        print("====> {} : {}".format(row, v_2))
                    break


def display_all_aliments(big_data):
    """
    'display_all_aliments' function is used to display all the aliments
    from the big data program.
    :param big_data:
    """
    aliment_name = big_data["user"]["aliment"]
    aliment_category = big_data["user"]["category"]
    display("~", 50, 2)
    print("En fonction de l'aliment {}".format(aliment_name))
    for aliment in big_data["console"]["aliments"][aliment_category].keys():
        if aliment == aliment_name:
            for key, value in big_data["console"]["rows"].items():
                if key == "local_category":
                    print("====> {} : {} ".format(value, aliment_category))
                else:
                    print("====> {} : {} "
                          .format(value, big_data["console"]["aliments"]
                                  [aliment_category][aliment_name][key]))


def display_substitute(big_data, substitute):
    """
    'display_substitute' function is used to display the substitute.
    :param big_data:
    :param substitute:
    """
    substitute_name = ""
    substitute_category = ""
    display_all_aliments(big_data)
    print("\nVoici le substitut proposé :")
    for key in substitute.keys():
        substitute_category = key
    for key in substitute[substitute_category].keys():
        substitute_name = key
    for key, value in big_data["console"]["rows"].items():
        if key == "local_category":
            print("====> {} : {} ".format(value, substitute_category))
        else:
            print("====> {} : {} "
                  .format(value, substitute[substitute_category][substitute_name][key]))
    display("~", 50, 2)


def display_historic(big_data):
    """
    'display_substitute' function is used to display the historic.
    :param big_data:
    :return:
    """
    big_data = load.read_table_historic(big_data)
    if len(big_data["console"]["historic"]["graphic"]) == 0:
        display("~", 50)
        print(" "*5+"~~~~~ L'historique est vide ~~~~~")
        display("~", 50)
    for key, value in big_data["console"]["historic"]["graphic"].items():
        print("REMPLACEMENT {}".format(key))
        display("*", 50)
        for k_1, v_1 in value.items():
            print("{}".format(k_1))
            i = 0
            for element in v_1[0]:
                row = big_data["console"]["historic"]["fr_rows"][i]
                print("====> {} : {} ".format(row, element))
                i += 1
            print("\n")
        display("*", 50)


def interface(big_data):
    """
    'interface' function drives the process
    towards each components of the console.
    :param big_data:
    """
    presentation()
    while 1:
        menu(big_data)


def start_program():
    """
    'start_program' gets the big data program
    to provide it to the interface.
    """
    display("*", 50, 5)
    print("Lancement de l'interface en cours...")
    display("*", 50, 5)
    the_instance = load.Loading()
    big_data = the_instance.big_data
    interface(big_data)
