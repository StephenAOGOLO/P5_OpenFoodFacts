import json
import requests
import logging as lg


def open_json_file(file):
    with open(file) as f:
        data = json.load(f)
    return data


def load_api_data():
    dict_data = {}
    list_c = ["product_name", "brands", "nutriscore_grade", "stores", "purchase_places", "url"]
    dict_data["sent"] = {}
    dict_data["rcvd"] = {}
    dict_data["sent"]["urls"] = open_json_file(".\\Packages\\urls.json")
    for url_name, url in dict_data["sent"]["urls"].items():
        response = requests.get(url)
        dict_data["rcvd"][url_name] = response.json()
    dict_data["rcvd"]["aliments"] = {}

    for url_name, url in dict_data["sent"]["urls"].items():
        dict_data["rcvd"]["aliments"][url_name] = {}
        for i in range(0, 20):
            dict_data["rcvd"]["aliments"][url_name][str(i)] = {}
            for element in list_c:
                if element in dict_data["rcvd"][url_name]["products"][i]:
                    dict_data["rcvd"]["aliments"][url_name][str(i)][element] = dict_data["rcvd"][url_name]["products"][i][element]
                else:
                    dict_data["rcvd"]["aliments"][url_name][str(i)][element] = "NOT_PROVIDED"
    dict_data = all_rows(dict_data)
    dict_data = all_categories(dict_data)
    dict_data = prepare_sql_values(dict_data)
    return dict_data


def all_categories(all_data):
    all_data["rcvd"]["local_category"]=[]
    for key in all_data["rcvd"]["aliments"].keys():
        all_data["rcvd"]["local_category"].append(key)
    return all_data


def all_rows(all_data):

    all_data["rcvd"]["rows"] = ["product_name",
                                "local_category",
                                "brands",
                                "nutriscore_grade",
                                "stores",
                                "purchase_places",
                                "url"
                                ]
    return all_data


def prepare_sql_values(all_data):
    list_categories = []
    all_data["rcvd"]["sql_values"] = {}
    for key in all_data["rcvd"]["aliments"].keys():
        all_data["rcvd"]["sql_values"][key] = {}
        list_categories.append(key)
    for category in list_categories:
        for i in range(0, 20):
            all_data["rcvd"]["sql_values"][category][category+"_"+str(i)] = all_data["rcvd"]["aliments"][category][str(i)]
    for category in list_categories:
        for i in range(0, 20):
            for row in all_data["rcvd"]["rows"]:
                try:
                    the_row = all_data["rcvd"]["sql_values"][category][category+"_"+str(i)][row]
                    the_row = str(the_row).replace(","," ou ")
                    the_row = the_row.replace("'","-")
                    all_data["rcvd"]["sql_values"][category][category + "_" + str(i)][row] = the_row
                except Exception as e:
                    lg.info("erreur sur part - ", e)
    for k, v in all_data["rcvd"]["sql_values"]["beurre"].items():
        lg.info("{} -> {}".format(k, v))
    return all_data
