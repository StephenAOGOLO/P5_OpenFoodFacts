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
    if choice == str(1):
        print("Vous avez choisi le menu 1")
        menu_1a(big_data)
    elif choice == str(2):
        print("Vous avez choisi le menu 2")
        menu_2a(big_data)
    elif choice == "x":
        print("Vous avez choisi de quitter le programme")
        quit_console()
    else:
        print("\nMauvaise saisie!!\nVous avez entré {}".format(choice,))


def menu_1a(big_data):
    """ Category"""
    display("*", 50, 5)
    while 1:
        print("Veuillez sélectionner la catégorie de votre aliment.")
        list_category = get_categories(big_data)
        print("\nx -  menu principal")
        choice = get_choice()
        if choice == "x":
            print("Vous avez choisi le retour au menu principal")
            menu(big_data)
        elif choice == "0":
        #elif choice is range(0, len(list_category)):
            print("Vous avez choisi la catégorie {}".format(choice))
            menu_1b(big_data)
        else:
            print("\nMauvaise saisie!!\nVous avez entré {}".format(choice))


def menu_1b(big_data):
    """Aliment"""
    display("*",50, 5)
    while 1:
        print("Veuillez sélectionner l'aliment'.")
        print("liste des aliments")
        print("\n0 -   menu principal")
        choice = get_choice()
        if choice == str(0):
            print("Vous avez choisi le retour au menu principal")
            menu(big_data)
        elif int(choice):
            print("Vous avez choisi l'aliment {}".format(choice))
            menu_1c(big_data)
        else:
            print("\nMauvaise saisie!!\nVous avez entré {}".format(choice))


def menu_1c(big_data):
    """Substitute"""
    display("*",50, 5)
    print("En fonction de l'aliment suivant :")
    print("Voici le substitut proposé")
    print("Voulez-vous le sauvegarder ?")
    print("1 - sauvegarder ?")
    print("0 - Retour au menu principal")
    choice = get_choice()
    if choice == str(0):
        print("Vous avez choisi le retour au menu principal")
        menu(big_data)
    if choice == str(1):
        print("Vous avez choisi l'aliment {}".format(choice))
        menu_1d(big_data)
    else:
        print("\nMauvaise saisie!!\nVous avez entré {}".format(choice))


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
    for i, e in enumerate(big_data["rcvd"]["local_category"]):
        print("{} - {}".format(i, e))
    list_category = big_data["rcvd"]["local_category"]
    return list_category


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
