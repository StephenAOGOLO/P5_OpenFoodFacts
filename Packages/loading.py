"""
Welcome to the loading module, 'loading.py'.
This module is especially composed of one function.
Which is used to initialize and feeds program parameters.
"""
# -*- coding: utf-8 -*-
from getpass4 import getpass as gp
import logging as lg
import Packages.mysql_operations as mo
import Packages.api_operations as ao
import Packages.options as opt
lg.basicConfig(level=lg.WARNING)


class Loading:
    """ Loading """
    def __init__(self):
        """init"""
        the_options = opt.Settings()
        self.params = the_options.get_data_file_ini("loading")
        self.root_status = self.params["root_access"]
        self.verify = self.params["check_db_exists"]
        self.user = self.params["user"]
        self.host = self.params["host"]
        self.pseudo = self.params["pseudo"]
        self.psw = self.params["psw"]
        self.db_name = self.params["db_name"]
        self.sql_file = self.params["db_sql_file"]
        self.urls_json_file = self.params["urls_json_file"]
        self.init_root()
        self.status = self.check_db(self.verify)
        self.mysql_session = mo.Mysql(self.user, self.psw, self.db_name)
        self.big_data = self.initialization()

    def initialization(self):
        """initialization"""
        self.big_data = self.get_all_data()
        return self.big_data

    def init_root(self):
        """init_root"""
        if self.root_status == "1":
            root_session = connect_root()
            is_user_created(root_session)

    def get_all_data(self):
        """get_all_data"""
        if self.status:
            api = ao.Data()
            data = api.big_data
            self.fill_table_category(data)
            self.fill_table_aliment(data)
        else:
            data = self.build_big_data()
        return data

    def build_big_data(self):
        """build_big_data"""
        data = {"rcvd": {}, "console": {}}
        data = ao.all_rows(data)
        data = ao.traduce_rows(data)
        data = self.read_table_category(data)
        data = self.read_table_aliment(data)
        data = ao.classify_ihm_values(data)
        return data

    def read_table_aliment(self, data):
        """read_table_aliment"""
        data["console"] = {}
        data["console"]["aliments"] = {}
        list_r = data["rcvd"]["rows"]
        for category in data["rcvd"]["local_category"]:
            where_clause = "local_category = '{}' ".format(category)
            list_content = self.mysql_session.select_from_where("*", "Aliment", where_clause)
            data["console"]["aliments"][category] = {}
            for e in list_content:
                data["console"]["aliments"][category][e[2]] = {list_r[0]: e[1], list_r[1]: e[3], list_r[2]: e[4],
                                                               list_r[3]: e[5], list_r[4]: e[6], list_r[5]: e[7],
                                                               list_r[6]: e[8]}
        return data

    def read_table_category(self, data):
        """read_table_category"""
        data["rcvd"]["local_category"] = []
        list_content = self.mysql_session.select_from("*", "Category")
        for index_tuple in range(1, len(list_content) + 1):
            for i, e in enumerate(list_content):
                if e[0] == str(index_tuple):
                    data["rcvd"]["local_category"].append(e[1])
                    continue
        return data

    def drop_tables(self):
        """drop_tables"""
        params = get_settings()
        user = params["user"]
        psw = params["psw"]
        db_name = params["db_name"]
        self.mysql_session = mo.Mysql(user, psw, db_name)
        self.mysql_session.executing("DROP TABLE IF EXISTS Historic")
        self.mysql_session.executing("DROP TABLE IF EXISTS Aliment")
        self.mysql_session.executing("DROP TABLE IF EXISTS Category")

    def create_tables(self, tables_data):
        """create_tables"""
        status = False
        self.drop_tables()
        for table, data in tables_data.items():
            status = self.mysql_session.executing(data)
        return status

    def check_db(self, check_status="0"):
        """check_db"""
        params = get_settings()
        user = params["user"]
        psw = params["psw"]
        self.mysql_session = mo.Mysql(user, psw)
        status = self.mysql_session.create_db()
        if check_status == "1":
            status = update_db(status)
            if not status:
                return status
        else:
            status = True
        contenu = self.open_sql_file()
        contenu = "".join(contenu)
        contenu = contenu.replace("\n", "")
        contenu = contenu.split(";")
        dict_tables = {"category": contenu[0], "aliment": contenu[1], "historic": contenu[2]}
        self.create_tables(dict_tables)
        return status

    def fill_table_category(self, data):
        """fill_table_category"""
        for i, category in enumerate(data["rcvd"]["local_category"]):
            pure_value = "('{}', '{}')".format(i + 1, category)
            self.mysql_session.insert_data("category", "(id, name)", pure_value)

    def fill_table_aliment(self, data):
        """fill_table_aliment"""
        for category in data["rcvd"]["local_category"]:
            for i in range(0, len(data["rcvd"]["sql_values"][category])):
                raw_data = ""
                data["rcvd"]["sql_values"][category + "_" + str(i)] = {}
                data["rcvd"]["sql_values"][category + "_" + str(i)]["pure_data"] = []
                data["rcvd"]["sql_values"][category + "_" + str(i)]["raw_data"] = ""
                i_rows = 0
                for k, v in data["rcvd"]["sql_values"][category][category + "_" + str(i)].items():
                    data["rcvd"]["sql_values"][category + "_" + str(i)]["pure_data"].append(v)
                    if i_rows == 0:
                        raw_data += v
                    else:
                        raw_data += ", " + v
                    i_rows += 1
                data["rcvd"]["sql_values"][category + "_" + str(i)]["raw_data"] = raw_data
                raw_data = ""
        for category in data["rcvd"]["local_category"]:
            for i in range(0, len(data["rcvd"]["sql_values"][category])):
                value = data["rcvd"]["sql_values"][category + "_" + str(i)]["raw_data"]
                if "EMPTY" in value:
                    continue
                if "NOT_PROVIDED" in value:
                    continue
                else:
                    value += "," + category
                    value += "," + category + "_" + str(i)
                    value = value.replace(",", "' , '")
                    pure_value = "('{}')".format(value)
                    self.mysql_session.insert_data("aliment", "(product_name, brands, nutriscore_grade,"
                                                   " stores, purchase_places, url, local_category,"
                                                   " local_name)", pure_value)



    def open_sql_file(self):
        """open_sql_file"""
        """ This function is used to open sql file.
        It's feeding the content file in a list.

        :return list_file: """

        with open(self.sql_file, "rt") as file:
            list_file = file.readlines()
        lg.info("=" * 150)
        lg.info("\nThere is the content file : {}\n".format(self.sql_file))
        for i, line in enumerate(list_file):
            lg.info("ligne {} : {}".format(i, line))
        lg.info("=" * 150)
        lg.info("\nEnd of file\n")
        lg.info("=" * 150)
        return list_file


def fill_table_historic(data):
    """fill_table_historic"""
    params = get_settings()
    user = params["user"]
    psw = params["psw"]
    db_name = params["db_name"]
    session = mo.Mysql(user, psw, db_name)
    aliment = data["save"]["aliment"]
    substitute = data["save"]["substitute"]
    where_clause_a = "local_name = '{}' ".format(aliment)
    where_clause_s = "local_name = '{}' ".format(substitute)
    aliment_id = session.select_from_where("id", "aliment", where_clause_a)
    substitute_id = session.select_from_where("id", "aliment", where_clause_s)
    aliment_id = int(aliment_id[0][0])
    substitute_id = int(substitute_id[0][0])
    pure_value = "('{}', '{}')".format(aliment_id, substitute_id)
    session.insert_data("historic", "(aliment_id, substitute_id)", pure_value)


def read_table_historic(data):
    """read_table_historic"""
    params = get_settings()
    user = params["user"]
    psw = params["psw"]
    db_name = params["db_name"]
    session = mo.Mysql(user, psw, db_name)
    data["console"]["historic"] = {}
    data["console"]["historic"]["swap_id"] = {}
    data["console"]["historic"]["graphic"] = {}
    data["console"]["historic"]["read_rows"] = read_columns(session)
    list_content = session.select_from("*", "Historic")
    for i, e in enumerate(list_content):
        lg.info("{} - {}".format(i, e))
        data["console"]["historic"]["swap_id"][str(e[0])] = {"aliment_id": e[1], "substitute_id": e[2]}
    for k, v in data["console"]["historic"]["swap_id"].items():
        where_clause_a = "id = '{}' ".format(v["aliment_id"])
        where_clause_s = "id = '{}' ".format(v["substitute_id"])
        aliment = session.select_from_where("*", "Aliment", where_clause_a)
        substitute = session.select_from_where("*", "Aliment", where_clause_s)
        data["console"]["historic"]["graphic"][k] = {"aliment": aliment, "substitute": substitute}
        lg.info("{} - {}".format(k, v))
    return data


def read_columns(session):
    """read_columns"""
    table = "INFORMATION_SCHEMA.COLUMNS"
    where_clause = "TABLE_NAME = 'Aliment' "
    t_rows = session.select_from_where("*", table, where_clause)
    i = 1
    read_rows = []
    while i < len(t_rows):
        for e in t_rows:
            if i == e[4]:
                read_rows.append(e[3])
                i += 1
    return read_rows


def is_user_created(root_session, host="localhost", user="stephen"):
    """is_user_created"""
    users = root_session.select_from("host, user", "mysql.user")
    there = False
    for e in users:
        if (e[0] == "localhost") and (str(e[1].decode()) == "stephen"):
            there = True
            break
    if not there:
        create_user(root_session)


def connect_root():
    """connect_root"""
    root_id = input("Veuillez entrer votre identifiant administrateur mysql : ")
    root_psw = gp("Veuillez entrer votre mot de passe administrateur mysql : ")
    root_session = mo.Mysql(root_id, root_psw)
    return root_session


def create_user(root_session, user="stephen", host="localhost", pseudo="stephen"):
    """create_user"""
    cmd = """CREATE USER '{}'@'{}' IDENTIFIED BY '{}'""".format(user, host, pseudo)
    status = root_session.executing(cmd)
    cmd = """GRANT ALL PRIVILEGES ON db_purebeurre.* TO 'stephen'@'localhost'"""
    root_session.executing(cmd)
    print("l'utilisateur '{}'@'{}' identifié en tant que '{}' a été créée ! "
          .format(user, host, pseudo))


def update_db(status):
    """update_db"""
    if status:
        while 1:
            print("Voulez-vous conserver la base de données actuelle ?")
            print("~"*50)
            print("==> Si vous répondez 'Oui', les informations proposées dans cette application"
                  " seront peut-être pas à jour."
                  "\n==> Si vous répondez 'Non', L'historique de vos aliments substitués"
                  " et toutes les autres informations seront réinitialisés.")
            print("~"*50)
            print("\n0 - Oui\n1 - Non\n")
            choice = input("Quel est votre choix : ")
            if choice == str(0):
                update_status = maintain_db(choice)
                return update_status
            elif choice == str(1):
                update_status = maintain_db(choice)
                return update_status
            else:
                print("\nMauvaise saisie!!\nVous avez entré {}".format(choice))
    return True


def maintain_db(choice):
    """maintain_db"""
    update_status = True
    if choice == str(0):
        print("La base de donnée actuelle va être utilisée !!")
        update_status = False
    else:
        print("La base de donnée actuelle va être réinitilalisée !!")
    return update_status


def get_settings():
    the_options = opt.Settings()
    params = the_options.get_data_file_ini("loading")
    return params


if __name__ == "__main__":
    the_instance = Loading()
    big_data = the_instance.big_data




