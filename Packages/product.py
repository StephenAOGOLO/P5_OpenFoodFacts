"""
Welcome to the product module, 'product.py'.
"""
# -*- coding: utf-8 -*-
import logging as lg
lg.basicConfig(level=lg.WARNING)


class Product:
    """
    Product class create an instance which contains
    all information concerning a product.
    It is also counting each new instance.
     """
    number = 0

    def __init__(self, name, local_c, brands, score, stores, places, url):
        """
        Init constructor has seven attributes.
        Theses attributes defines a product.
        """
        self.name = name
        self.local_category = local_c
        self.brands = brands
        self.score = score
        self.stores = stores
        self.places = places
        self.url = url
        Product.number += 1

    def __repr__(self):
        """
        This method is formating a new display
        by using : __repr__ .
        :return:
        """
        return "\nVoici les détails du produit:" \
               "nom: {}\ncategorie: {}\nmarque: {}\nnutriscore:" \
               " {}\nmagasins: {}\nLieu: {}\nSite: {}\n"\
            .format(self.name,
                    self.local_category,
                    self.brands,
                    self.score,
                    self.stores,
                    self.places,
                    self.url)

    def __lt__(self, second):
        """
        This method is comparing score attribute
         by using : __lt__ .
        :param second:
        :return:
        """
        if self.score < second.score:
            return True
        return False


def get_product_number():
    """
    get_product_number
    """
    print("Il y a {} produits au total".format(Product.number))
