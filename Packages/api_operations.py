"""
Welcome to the API Operations module, 'api_operations.py'.
This module is composed of 'Data' class.
three methods are defined to retrieve and store data
coming from OpFoFa - OpenFoodFacts server.
ten functions are defined to slice and sort the data
needed for each packages module.
"""
# -*- coding: utf-8 -*-
import logging as lg
import json
import requests


class Data:
    """
    Data class create an instance which centralizing
    all pure data coming from Openfoodfacts server.
    """
    def __init__(self):
        """
        Init constructor has two attributes:
        json_url_file : URLS file path needed to request OpFoFa server.
        big_data : Containing OpFoFa response, sliced and sorted.
        'big_data' is a dict.
        """
        self.json_url_file = ".\\Packages\\urls.json"
        self.big_data = self.load_api_data()

    def load_api_data(self):
        """
        'Load_api_data' method is containing every steps of
         getting, slicing and sorting
         before the data providing.
         """
        all_data = {"sent": {}, "rcvd": {}}
        all_data = self.request_urls(all_data)
        print("La récupération des données depuis le serveur OpenFoodFacts est en cours...")
        all_data = response_urls(all_data)
        all_data["rcvd"]["aliments"] = {}
        print("Récupération des données terminée OpenFoodFacts avec succès")
        print("Organisation des données en cours...")
        all_data = get_aliments(all_data)
        print("Préparation des données pour l'interface en cours...")
        print("Préparation des données pour la base de données en cours...")
        all_data = all_rows(all_data)
        all_data = all_categories(all_data)
        all_data = prepare_sql_values(all_data)
        all_data = prepare_hmi_values(all_data)
        all_data = classify_ihm_values(all_data)
        print("Préparation des données terminée!!!")
        print("Initialisation du système terminée avec succès.\n")
        return all_data

    def open_json_file(self):
        """'open_json_file' method read a given json file.
        It returns the content file into a dict."""
        with open(self.json_url_file) as file:
            data = json.load(file)
        return data

    def request_urls(self, all_data):
        """
        'request_urls' method adds url requests into the big data
        :param all_data:
        :return all_data:
        """
        all_data["sent"]["urls"] = self.open_json_file()
        return all_data


def response_urls(all_data):
    """
    'response_urls' method execute each url request.
    Each response is stored into the big data.
    :param all_data:
    :return all_data:
    """
    for url_name, url in all_data["sent"]["urls"].items():
        response = requests.get(url)
        all_data["rcvd"][url_name] = response.json()
    return all_data


def get_aliments(data):
    """
    'get_aliments' method analyses each OpFoFa response
    and catches all aliments located in.
    These aliments are sorted by quality.
    Actually, some aliments info may not be provided.
    If it is so, this method set 'EMPTY' and 'NOT_PROVIDED'
    tags in the impacted field. All aliment information
    are stored in to the big data.
    Keys to find '["rcvd"]["aliments"]'.
    :param data:
    :return data:
    """
    list_r = ["product_name", "brands", "nutriscore_grade",
              "stores", "purchase_places", "url"]
    for url_name in data["sent"]["urls"].keys():
        data["rcvd"]["aliments"][url_name] = {}
        for i in range(0, len(data["rcvd"][url_name]["products"])):
            data["rcvd"]["aliments"][url_name][str(i)] = {}
            for element in list_r:
                if element in data["rcvd"][url_name]["products"][i]:
                    if data["rcvd"][url_name]["products"][i][element] == "":
                        data["rcvd"]["aliments"][url_name][str(i)][element]\
                            = "EMPTY"
                    else:
                        data["rcvd"]["aliments"][url_name][str(i)][element] = \
                            data["rcvd"][url_name]["products"][i][element]
                else:
                    data["rcvd"]["aliments"][url_name][str(i)][element]\
                        = "NOT_PROVIDED"
    return data


def all_categories(all_data):
    """
    'all_categories' method stores every aliment categories into a list.
    Keys to find '["rcvd"]["local_category"]'.
    :param all_data:
    :return all_data:
    """
    all_data["rcvd"]["local_category"] = []
    for key in all_data["rcvd"]["aliments"].keys():
        all_data["rcvd"]["local_category"].append(key)
    return all_data


def all_rows(all_data):
    """
    'all_rows' method provide and stores every aliment criteria into a list.
    Keys to find '["rcvd"]["rows"]'.
    :param all_data:
    :return all_data:
    """
    all_data["rcvd"]["rows"] = [
        "product_name", "local_category", "brands", "nutriscore_grade",
        "stores", "purchase_places", "url"
        ]
    return all_data


def prepare_sql_values(data):
    """
    'prepare_sql_values' method formats all needed data
    to fill MYSQL tables. Keys to find '["rcvd"]["sql_values"]'.
    :param data:
    :return data:
    """
    list_categories = []
    data["rcvd"]["sql_values"] = {}
    for key in data["rcvd"]["aliments"].keys():
        data["rcvd"]["sql_values"][key] = {}
        list_categories.append(key)
    for category in list_categories:
        for i in range(0, len(data["rcvd"]["aliments"][category])):
            data["rcvd"]["sql_values"][category][category+"_"+str(i)]\
                = data["rcvd"]["aliments"][category][str(i)]
    for category in list_categories:
        for i in range(0, len(data["rcvd"]["aliments"][category])):
            for row in data["rcvd"]["rows"]:
                try:
                    the_row = data["rcvd"]["sql_values"][category][category+"_"+str(i)][row]
                    the_row = str(the_row).replace(",", " ou ")
                    the_row = the_row.replace("'", "-")
                    data["rcvd"]["sql_values"][category][category + "_" + str(i)][row] = the_row
                except KeyError as error:
                    lg.info("erreur sur part: %s", error)
    return data


def prepare_hmi_values(all_data):
    """
    'prepare_hmi_values' function formats all needed data
    to display it through the interface. Keys to find '["console"]'.
    :param all_data:
    :return:
    """
    all_data["console"] = {}
    all_data["console"]["aliments"] = {}
    list_c = all_data["rcvd"]["local_category"]
    for category in list_c:
        all_data["console"]["aliments"][category] = {}
        for key, value in all_data["rcvd"]["sql_values"][category].items():
            lg.info("\n%s = %s", key, value)
            if "EMPTY" in value.values():
                continue
            if "NOT_PROVIDED" in value.values():
                continue
            all_data["console"]["aliments"][category][key] = value
    return all_data


def classify_ihm_values(all_data):
    """
    'classify_ihm_values' function sorts all needed data
    to display it through the interface. This function set
    the substitute aliment into the big data.
    Keys to find '["console"]["substitute"]'.
    :param all_data:
    :return all_data:
    """
    dict_substitute = set_substitute(all_data)
    all_data["console"]["substitute"] = dict_substitute
    traduce_rows(all_data)
    return all_data


def set_substitute(all_data):
    """
    'set_substitute' function finds and stores all aliment substitutes.
    These substitutes are stored into a dict.
    Keys to find '["console"]["substitute"]'
    :param all_data:
    :return dict_substitutes:
    """
    dict_substitutes = {}
    for key, value in all_data["console"]["aliments"].items():
        score = "g"
        for key_2, value_2 in value.items():
            if value_2["nutriscore_grade"] < score:
                substitute = key_2
                info = value_2
                score = value_2["nutriscore_grade"]
        dict_substitutes[key] = {}
        dict_substitutes[key][substitute] = info
    return dict_substitutes


def traduce_rows(all_data):
    """
    'traduce_rows' function traduces every aliment criteria in french.
    Keys to find '["console"]["rows"]'.
    :param all_data:
    :return:
    """
    list_fr_r = ["Nom", "Catégorie", "Marque",
                 "Nutriscore", "Magasins", "Lieu", "URL"]
    all_data["console"]["rows"] = {}
    for i, element in enumerate(all_data["rcvd"]["rows"]):
        all_data["console"]["rows"][element] = list_fr_r[i]
    return all_data


def show_all_data(all_data):
    """
    'show_all_data' function starts recursive operations
    to display the big data tree. This function is only
    use for debug. It is not called in the default program process.
    :param all_data:
    :return True:
    """
    num = 0
    if isinstance(all_data) == dict:
        for key, value in all_data.items():
            level = "="*num
            print(level+"> {} => {}".format(key, value))
            print("*"*50)
            if isinstance(value) == dict:
                show_all_data(value)
            num += 1
    else:
        print("*"*50)
        print("Fonction show_all_data(element)")
        print("element n'est pas un dict...")
        print("*" * 50)
    return True
