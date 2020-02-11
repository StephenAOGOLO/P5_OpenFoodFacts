import Packages.mysql_operations as mo
import Packages.api_operations as ao


def fill_table_category():
    ## TABLE CATEGORY
    session = mo.Mysql("stephen", "stephen")
    dico = ao.load_api_data()
    for i, category in enumerate(dico["rcvd"]["local_category"]):
        pure_value = "('{}', '{}')".format(i+1, category)
        session.insert_data("category", "(id, name)", pure_value)


def fill_table_aliment():

    # TABLE ALIMENT
    session = mo.Mysql("stephen", "stephen")
    dico = ao.load_api_data()
    for category in dico["rcvd"]["local_category"]:
        for i in range(0, 20):
            raw_data = ""
            dico["rcvd"]["sql_values"][category + "_" + str(i)] = {}
            dico["rcvd"]["sql_values"][category + "_" + str(i)]["pure_data"] = []
            dico["rcvd"]["sql_values"][category + "_" + str(i)]["raw_data"] = ""
            i_rows = 0
            for k, v in dico["rcvd"]["sql_values"][category][category+"_"+str(i)].items():
                dico["rcvd"]["sql_values"][category + "_" + str(i)]["pure_data"].append(v)
                if i_rows == 0:
                    raw_data += v
                else:
                    raw_data += ", " + v
                i_rows += 1
            dico["rcvd"]["sql_values"][category + "_" + str(i)]["raw_data"] = raw_data
            raw_data = ""
    for i in range(0, 20):
        for category in dico["rcvd"]["local_category"]:
            value = dico["rcvd"]["sql_values"][category + "_" + str(i)]["raw_data"]
            value += ","+category
            value += "," + category + "_" + str(i)
            value = value.replace(",", "' , '")
            pure_value = "('{}')".format(value)
            session.insert_data("aliment", "(product_name, brands, nutriscore_grade, stores, purchase_places, url, local_category, local_name)", pure_value)


if __name__ == "__main__":
    fill_table_category()
    fill_table_aliment()