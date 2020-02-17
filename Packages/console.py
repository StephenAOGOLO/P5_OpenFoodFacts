"""Console"""
# -*- coding: utf-8 -*-
import os
import Packages.api_operations as ao
import Packages.loading as load


def menu_1(big_data):
    """ Aliment to switch"""
    while 1:
        display_stars()
        print("> **menu_1**\n")
        print("> **Quel aliment souhaitez-vous remplacer ?**")
        display_stars()
        print("Veuillez sélectionner la catégorie de votre aliment.")
        #print("liste des categories...")
        get_categories(big_data)
        print("\nx -  menu principal")
        choice = get_choice()
        if choice == "x":
            print("Vous avez choisi le retour au menu principal")
            menu(big_data)
        elif int(choice):
            print("Vous avez choisi la catégorie {}".format(choice))
            menu_1_category(big_data)
        else:
            print("\nMauvaise saisie!!\nVous avez entré {}".format(choice))


def menu_2(big_data):
    """Aliment to substitute"""
    print("> **menu_2**\n")


def menu_1_category(big_data):
    """Category"""
    print("> **menu_category**\n")
    while 1:
        display_stars()
        print("> **menu_1**\n")
        print("> **Quel aliment souhaitez-vous remplacer ?**")
        display_stars()
        print("Veuillez sélectionner l'aliment'.")
        print("liste des aliments")
        print("\n0 -   menu principal")
        choice = get_choice()
        if choice == str(0):
            print("Vous avez choisi le retour au menu principal")
            menu(big_data)
        elif int(choice):
            print("Vous avez choisi l'aliment {}".format(choice))
            menu_1_aliment(big_data)
        else:
            print("\nMauvaise saisie!!\nVous avez entré {}".format(choice))


def menu_1_aliment(big_data):
    """Aliment"""
    print("En fonction de cet l'aliment")
    print("Voici le substitut proposé")
    print("*"*50)
    print("*"*50)
    print("Voulez-vous le sauvegarder ?")
    print("1 - sauvegarder ?")
    print("0 - Retour au menu principal")
    choice = get_choice()
    if choice == str(0):
        print("Vous avez choisi le retour au menu principal")
        menu(big_data)
    if choice == str(1):
        print("Vous avez choisi l'aliment {}".format(choice))
        menu_1_save(big_data)
    else:
        print("\nMauvaise saisie!!\nVous avez entré {}".format(choice))


def menu_1_substitute(big_data):
    """Substitute"""
    print("> **menu_substitute**\n")


def menu_1_save(big_data):
    """Save"""
    print("> **menu_save**\n")
    display_stars()
    print("l'aliment et son substitut ont été sauvegardé !")
    display_stars()
    menu(big_data)


def menu_2_historic(big_data):
    """Historic"""
    print("> **menu_historic**\n")
    print("\n")
    print("Voici l'historique des aliments substitués")
    for i in range(0, 5):
        display_stars()
    print("0 - Menu principal.")
    choice = get_choice()
    if choice == str(0):
        print("Vous avez choisi le menu 0")
        menu(big_data)
    else:
        print("\nMauvaise saisie!!\nVous avez entré {}".format(choice,))
        menu_2_historic(big_data)


def menu(big_data):
    """Menu"""
    print("1 - Quel aliment souhaitez-vous remplacer ?")
    print("2 - Retrouver mes aliments subtitués.")
    choice = get_choice()
    if choice == str(1):
        print("Vous avez choisi le menu 1")
        menu_1(big_data)
    elif choice == str(2):
        print("Vous avez choisi le menu 2")
        menu_2_historic(big_data)
    else:
        print("\nMauvaise saisie!!\nVous avez entré {}".format(choice,))


def presentation():
    """Presentation"""
    display_stars()
    print("****BIENVENUE SUR PUREBERRE app ****")
    display_stars()


def display_stars(number=50):
    print("*"*number)


def clear_screen():
    os.system("CLS")


def get_choice():
    """Text entry"""
    text = input("Que voulez-vous faire : ")
    display_stars()
    return text


def start_program():
    display_stars()
    print("interface running...")
    display_stars()
    big_data = load.initialization()
    interface(big_data)


def get_categories(big_data):
    """Categories"""
    for i, e in enumerate(big_data["rcvd"]["local_category"]):
        print("{} - {}".format(i, e))


def interface(big_data):
    """Interface"""
    presentation()
    quit = False
    while not quit:
        menu(big_data)
    quit = True
    return quit


if __name__ == "__main__":
    start_program()