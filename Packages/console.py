"""Console"""
# -*- coding: utf-8 -*-
import os
import Packages.api_operations as ao


def menu_1():
    """ Aliment to switch"""
    while 1:
        display_stars()
        print("> **menu_1**\n")
        print("> **Quel aliment souhaitez-vous remplacer ?**")
        display_stars()
        print("Veuillez sélectionner la catégorie de votre aliment.")
        print("liste des categories...")
        print("\nTapez 0 pour retourner au menu principale")
        choice = get_choice()
        if choice == str(0):
            print("Vous avez choisi le retour au menu principal")
            menu()
        elif int(choice):
            print("Vous avez choisi la catégorie {}".format(choice))
            menu_2_historic()
        else:
            print("\nMauvaise saisie!!\nVous avez entré {}".format(choice))


def menu_2():
    """Aliment to substitute"""
    print("> **menu_2**\n")


def menu_1_category():
    """Category"""
    print("> **menu_category**\n")


def menu_1_aliment():
    """Aliment"""
    print("> **menu_aliment**\n")


def menu_1_substitute():
    """Substitute"""
    print("> **menu_substitute**\n")


def menu_1_save():
    """Save"""
    print("> **menu_save**\n")


def menu_2_historic():
    """Historic"""
    print("> **menu_historic**\n")


def menu():
    """Menu"""
    print("1 - Quel aliment souhaitez-vous remplacer ?")
    print("2 - Retrouver mes aliments subtitués.")
    choice = get_choice()
    if choice == str(1):
        print("Vous avez choisi le menu 1")
        menu_1()
    elif choice == str(2):
        print("Vous avez choisi le menu 2")
        menu_2_historic()
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
    print("*" * 50)
    ao.load_api_data()
    interface()


def get_categories():
    """Categories"""
    pass


def interface():
    """Interface"""
    presentation()
    quit = False
    while not quit:
        menu()
    quit = True
    return quit


if __name__ == "__main__":
    start_program()