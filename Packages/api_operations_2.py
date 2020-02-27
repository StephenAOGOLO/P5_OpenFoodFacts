import json
import requests
import logging as lg

class Data:
    """Data"""
    def __init__(self):
        """init"""
        self.big_data = load_api_data()

def open_json_file(file):
    with open(file) as f:
        data = json.load(f)
    return data


def request_urls(all_data):
    all_data["sent"]["urls"] = open_json_file(".\\Packages\\urls.json")
    return all_data


def response_urls(all_data):
    for url_name, url in all_data["sent"]["urls"].items():
        response = requests.get(url)
        all_data["rcvd"][url_name] = response.json()
    return all_data


def get_aliments(all_data):
    list_r = ["product_name", "brands", "nutriscore_grade", "stores", "purchase_places", "url"]
    for url_name, url in all_data["sent"]["urls"].items():
        all_data["rcvd"]["aliments"][url_name] = {}
        for i in range(0, len(all_data["rcvd"][url_name]["products"])):
            all_data["rcvd"]["aliments"][url_name][str(i)] = {}
            for element in list_r:
                if element in all_data["rcvd"][url_name]["products"][i]:
                    if all_data["rcvd"][url_name]["products"][i][element] == "":
                        all_data["rcvd"]["aliments"][url_name][str(i)][element] = "EMPTY"
                    else:
                        all_data["rcvd"]["aliments"][url_name][str(i)][element] = all_data["rcvd"][url_name]["products"][i][element]
                else:
                    all_data["rcvd"]["aliments"][url_name][str(i)][element] = "NOT_PROVIDED"
    return all_data


def load_api_data():
    all_data = {}
    all_data["sent"] = {}
    all_data["rcvd"] = {}
    all_data = request_urls(all_data)
    print("Retrieving data from OpenFoodFacts server in progress...")
    all_data = response_urls(all_data)
    all_data["rcvd"]["aliments"] = {}
    print("Data received from OpenFoodFacts server")
    print("Data organizing in progress...")
    all_data = get_aliments(all_data)
    print("Getting data ready for console and local database...")
    all_data = all_rows(all_data)
    all_data = all_categories(all_data)
    all_data = prepare_sql_values(all_data)
    all_data = prepare_ihm_values(all_data)
    all_data = classify_ihm_values(all_data)
    print("Data ready!!!")
    print("Data initialization complete.")
    return all_data


def all_categories(all_data):
    all_data["rcvd"]["local_category"] = []
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


def provide_categories(all_data):

    all_data["console"]["aliments"]["categories"] = {}
    for i, element in enumerate(all_data["rcvd"]["local_category"]):
        lg.info("{} - {}".format(i, element))
        all_data["console"]["aliments"]["categories"][i] = element
    return all_data["console"]["aliments"]["categories"]


def prepare_sql_values(all_data):
    list_categories = []
    all_data["rcvd"]["sql_values"] = {}
    for key in all_data["rcvd"]["aliments"].keys():
        all_data["rcvd"]["sql_values"][key] = {}
        list_categories.append(key)
    for category in list_categories:
        for i in range(0, len(all_data["rcvd"]["aliments"][category])):
            all_data["rcvd"]["sql_values"][category][category+"_"+str(i)] = all_data["rcvd"]["aliments"][category][str(i)]
    for category in list_categories:
        for i in range(0, len(all_data["rcvd"]["aliments"][category])):
            for row in all_data["rcvd"]["rows"]:
                try:
                    the_row = all_data["rcvd"]["sql_values"][category][category+"_"+str(i)][row]
                    the_row = str(the_row).replace(","," ou ")
                    the_row = the_row.replace("'","-")
                    all_data["rcvd"]["sql_values"][category][category + "_" + str(i)][row] = the_row
                except Exception as e:
                    lg.info("erreur sur part - ", e)
    return all_data


def prepare_ihm_values(all_data):
    all_data["console"] = {}
    all_data["console"]["aliments"] = {}
    list_c = all_data["rcvd"]["local_category"]
    list_r = all_data["rcvd"]["rows"]
    for i, category in enumerate(list_c):
        all_data["console"]["aliments"][category] = {}
        for k, v in all_data["rcvd"]["sql_values"][category].items():
            lg.info("\n{} = {}".format(k, v))
            if "EMPTY" in v.values():
                continue
            if "NOT_PROVIDED" in v.values():
                continue
            else:
                all_data["console"]["aliments"][category][k] = v
    return all_data


def classify_ihm_values(all_data):
    """Classify IHM data """

    dict_substitute = set_substitute(all_data)
    all_data["console"]["substitute"] = dict_substitute
    traduce_rows(all_data)
    return all_data


def off_set_substitute(all_data):
    dict_substitutes = {}
    substitute = "g"
    for k, v in all_data["console"]["aliments"].items():
        for ke, va in v.items():
            if va["nutriscore_grade"] < substitute:
                substitute = ke
                score = va
        dict_substitutes[k] = {}
        dict_substitutes[k][substitute] = score
    return dict_substitutes


def set_substitute(all_data):
    dict_substitutes = {}
    for k, v in all_data["console"]["aliments"].items():
        score = "g"
        for ke, va in v.items():
            if va["nutriscore_grade"] < score:
                substitute = ke
                info = va
                score = va["nutriscore_grade"]
        dict_substitutes[k] = {}
        dict_substitutes[k][substitute] = info
    return dict_substitutes


def traduce_rows(all_data):
    list_fr_r = ["Nom", "Catégorie", "Marque", "Nutriscore", "Magasins", "Lieu", "URL"]
    all_data["console"]["rows"] = {}
    for i, e in enumerate(all_data["rcvd"]["rows"]):
        all_data["console"]["rows"][e] = list_fr_r[i]
    return all_data


def show_all_data(all_data):
    num = 0
    if type(all_data) == dict:
        for k, v in all_data.items():
            level = "="*num
            print(level+"> {} => {}".format(k, v))
            print("*"*50)
            if type(v) == dict:
                show_all_data(v)
            num += 1
    else:
        print("*"*50)
        print("Fonction show_all_data(element)")
        print("element n'est pas un dict...")
        print("*" * 50)
    return 0


if __name__ == "__main__":

    dico = load_api_data()
    show_all_data(dico)
