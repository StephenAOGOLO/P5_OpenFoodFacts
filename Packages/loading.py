"""
Welcome to the loading module, 'loading.py'.
This module is composed of one class 'Loading'.
Twelve methods to handle every input/output modules data.
Eight methods to handle every input/output modules data.
"""
# -*- coding: utf-8 -*-
import logging as lg
from getpass4 import getpass as gp
import Packages.mysql_operations as mo
import Packages.api_operations as ao
import Packages.options as opt
import Packages.product as prd
lg.basicConfig(level=lg.WARNING)


class Loading:
    """Loading class create an instance which managing
     steps initialization."""
    def __init__(self):
        """
        Init constructor has thirteen attributes.
        These attributes are picking parameters located into the external settings ini file.
        """
        the_options = opt.Settings()
        self.params = the_options.get_data_file_ini("loading")
        self.init_root()
        self.status = self.check_db(self.params["check_db_exists"])
        self.mysql_session = mo.Mysql(self.params["user"],
                                      self.params["psw"],
                                      self.params["db_name"])
        self.big_data = self.initialization()

    def initialization(self):
        """
        'initialization' method sets as attribute the big data.
        :return self.big_data:
        """
        self.big_data = self.get_all_data()
        return self.big_data

    def init_root(self):
        """
        'init_root' method activate the root mode
        only if self.root_status is on.
        """
        if self.params["root_access"] == "1":
            root_session = connect_root()
            params = get_settings()
            usr = params["root_user_db"]
            hst = params["root_host_db"]
            is_user_created(root_session, hst, usr)

    def get_all_data(self):
        """
        'get_all_data' method builds the local database and
        fills it if self.status is on. It read the local database
        if self.status is off. It either returns the big data from
        OpFoFa server either the big data read from the existing
        local database.
        :return:
        """
        if self.status:
            api = ao.Data()
            data = api.big_data
            self.fill_table_category(data)
            self.fill_table_aliment(data)
        else:
            data = self.build_big_data()
        data = build_products(data)
        prd.get_product_number()
        return data

    def build_big_data(self):
        """
        'build_big_data' method provides the big data
        read from the existing local database.
        :return:
        """
        data = {"rcvd": {}, "console": {}}
        data = ao.all_rows(data)
        data = ao.traduce_rows(data)
        data = self.read_table_category(data)
        data = self.read_table_aliment(data)
        data = ao.classify_ihm_values(data)
        return data

    def read_table_aliment(self, data):
        """
        'read_table_aliment' method reads
         all needed data from table 'Aliment'.
         It returns the data into a dict.
        :param data:
        :return:
        """
        data["console"] = {}
        data["console"]["aliments"] = {}
        list_r = data["rcvd"]["rows"]
        for category in data["rcvd"]["local_category"]:
            where_clause = "local_category = '{}' ".format(category)
            list_content = self.mysql_session.select_from_where("*", "Aliment", where_clause)
            data["console"]["aliments"][category] = {}
            for element in list_content:
                data["console"]["aliments"][category][element[2]] = {
                    list_r[0]: element[1], list_r[1]: element[3], list_r[2]: element[4],
                    list_r[3]: element[5], list_r[4]: element[6], list_r[5]: element[7],
                    list_r[6]: element[8]}
        return data

    def read_table_category(self, data):
        """
        'read_table_category' method reads
         all needed data from table 'Category'.
         It returns the data into a dict.
        :param data:
        :return:
        """
        data["rcvd"]["local_category"] = []
        list_content = self.mysql_session.select_from("*", "Category")
        for index_tuple in range(1, len(list_content) + 1):
            for element in list_content:
                if element[0] == str(index_tuple):
                    data["rcvd"]["local_category"].append(element[1])
                    continue
        return data

    def drop_tables(self):
        """
        'drop_tables' method erases all database tables.
        """
        params = get_settings()
        user = params["user"]
        psw = params["psw"]
        db_name = params["db_name"]
        self.mysql_session = mo.Mysql(user, psw, db_name)
        self.mysql_session.executing("DROP TABLE IF EXISTS Historic")
        self.mysql_session.executing("DROP TABLE IF EXISTS Aliment")
        self.mysql_session.executing("DROP TABLE IF EXISTS Category")

    def create_tables(self, tables_data):
        """
        'create_tables' method creates all database tables.
        It returns status execution.
        :param tables_data:
        :return status:
        """
        status = False
        self.drop_tables()
        for data in tables_data.values():
            status = self.mysql_session.executing(data)
        return status

    def check_db(self, check_status="0"):
        """
        'check_db' method determines the database existence.
        If so, the method drives the process toward a database
        creation choice. If not so, the method drives
        the process toward the database creation.
        It returns the process status .
        :param check_status:
        :return:
        """
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
        """
        'fill_table_category' method insert
         all concerning data into table 'Category'.
        :param data:
        """
        for i, category in enumerate(data["rcvd"]["local_category"]):
            pure_value = "('{}', '{}')".format(i + 1, category)
            self.mysql_session.insert_data("category", "(id, name)", pure_value)

    def fill_table_aliment(self, data):
        """
        'fill_table_aliment' method insert
         all concerning data into table 'Aliment'.
        :param data:
        """
        for category in data["rcvd"]["local_category"]:
            for i in range(0, len(data["rcvd"]["sql_values"][category])):
                raw_data = ""
                data["rcvd"]["sql_values"][category + "_" + str(i)] = {}
                data["rcvd"]["sql_values"][category + "_" + str(i)]["pure_data"] = []
                data["rcvd"]["sql_values"][category + "_" + str(i)]["raw_data"] = ""
                i_rows = 0
                for value in data["rcvd"]["sql_values"][category][category + "_" + str(i)].values():
                    data["rcvd"]["sql_values"][category + "_" + str(i)]["pure_data"].append(value)
                    if i_rows == 0:
                        raw_data += value
                    else:
                        raw_data += ", " + value
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
                value += "," + category
                value += "," + category + "_" + str(i)
                value = value.replace(",", "' , '")
                pure_value = "('{}')".format(value)
                self.mysql_session.insert_data(
                    "aliment", "(product_name, brands, nutriscore_grade,"
                               " stores, purchase_places, url, local_category,"
                               " local_name)", pure_value)

    def open_sql_file(self):
        """
        'open_sql_file' method opens sql file.
        It returns the content file in a list.
        :return:
        """
        with open(self.params["db_sql_file"], "rt") as file:
            list_file = file.readlines()
        lg.info("=" * 150)
        lg.info("\nThere is the content file : %s\n", self.params["db_sql_file"])
        for i, line in enumerate(list_file):
            lg.info("ligne %s : %s", i, line)
        lg.info("=" * 150)
        lg.info("\nEnd of file\n")
        lg.info("=" * 150)
        return list_file


def build_products(data):
    """
    'build_products' function provides each aliment
     as an product object. It returns all theses products
    into the big data.
    :param data:
    :return:
    """
    data["objects"] = {}
    for category, value in data["console"]["aliments"].items():
        data["objects"][category] = {}
        for local_n, rows in value.items():
            name = rows["product_name"]
            local_c = category
            brands = rows["brands"]
            score = rows["nutriscore_grade"]
            stores = rows["stores"]
            places = rows["purchase_places"]
            url = rows["url"]
            product = prd.Product(name, local_c, brands, score, stores, places, url)
            data["objects"][category][local_n] = product
    return data


def fill_table_historic(data):
    """
    'fill_table_historic' function insert
    all concerning data into table 'Historic'.
    :param data:
    """
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
    """
    'read_table_historic' function reads
    all needed data from table 'Historic'.
    It returns the data into a dict.
    :param data:
    :return:
    """
    params = get_settings()
    user = params["user"]
    psw = params["psw"]
    db_name = params["db_name"]
    session = mo.Mysql(user, psw, db_name)
    data["console"]["historic"] = {}
    data["console"]["historic"]["swap_id"] = {}
    data["console"]["historic"]["graphic"] = {}
    data["console"]["historic"]["read_rows"] = read_columns(session)
    data["console"]["historic"]["fr_rows"] = fr_columns()
    list_content = session.select_from("*", "Historic")
    for i, element in enumerate(list_content):
        lg.info("%s - %s", i, element)
        data["console"]["historic"]["swap_id"][str(element[0])] =\
            {"aliment_id": element[1], "substitute_id": element[2]}
    for key, value in data["console"]["historic"]["swap_id"].items():
        where_clause_a = "id = '{}' ".format(value["aliment_id"])
        where_clause_s = "id = '{}' ".format(value["substitute_id"])
        aliment = session.select_from_where("*", "Aliment", where_clause_a)
        substitute = session.select_from_where("*", "Aliment", where_clause_s)
        data["console"]["historic"]["graphic"][key] = {"aliment": aliment, "substitute": substitute}
        lg.info("%s - %s", key, value)
    return data


def read_columns(session):
    """
    'read_columns' function reads
    all columns from table 'Aliment'.
    It returns the data into a list.
    :param session:
    :return:
    """
    table = "INFORMATION_SCHEMA.COLUMNS"
    where_clause = "TABLE_NAME = 'Aliment' "
    t_rows = session.select_from_where("*", table, where_clause)
    i = 1
    read_rows = []
    while i < len(t_rows):
        for element in t_rows:
            if i == element[4]:
                read_rows.append(element[3])
                i += 1
    return read_rows


def fr_columns():
    """
    'fr_columns' function provides
    all columns from table 'Aliment'
    in french. It returns the data into a list.
    :return:
    """
    columns = ["Id", "Nom", "Tag", "Categorie",
               "Marque", "Nutriscore", "Magasin",
               "Lieu", "Site"]
    return columns


def is_user_created(root_session, host="localhost", user="stephen"):
    """
    'is_user_created' function checks if the MYSQL user
    given as parameter is existing into MYSQL server.
    :param root_session:
    :param host:
    :param user:
    """
    users = root_session.select_from("host, user", "mysql.user")
    there = False
    for element in users:
        if (element[0] == host) and (str(element[1].decode()) == user):
            there = True
            break
    if not there:
        params = get_settings()
        usr = params["root_user_db"]
        hst = params["root_host_db"]
        psw = params["root_psw_db"]
        create_user(root_session, usr, hst, psw)


def connect_root():
    """
    'connect_root' function prompts the program user
    to enter his MYSQL root credentials.
    It returns the opened root session.
    :return:
    """
    root_id = input("Veuillez entrer votre identifiant administrateur mysql : ")
    root_psw = gp("Veuillez entrer votre mot de passe administrateur mysql : ")
    root_session = mo.Mysql(root_id, root_psw)
    return root_session


def create_user(root_session, user="stephen", host="localhost",
                passwd="stephen", db_name="db_purebeurre"):
    """
    'create_user' function creates a MYSQL user.
    :param root_session:
    :param user:
    :param host:
    :param passwd:
    :param db_name:
    """
    cmd = """CREATE USER '{}'@'{}' IDENTIFIED BY '{}'""".format(user, host, str(passwd))
    root_session.executing(cmd)
    cmd = """GRANT ALL PRIVILEGES ON {}.* TO '{}'@'{}'""".format(db_name, user, host)
    root_session.executing(cmd)
    print("l'utilisateur '{}'@'{}' a été créée ! "
          .format(user, host))


def update_db(status):
    """
    'update_db' prompts the program user
    either to keep the existing database
    or reset it.
    :param status:
    :return:
    """
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
            if choice == str(1):
                update_status = maintain_db(choice)
                return update_status
            print("\nMauvaise saisie!!\nVous avez entré {}".format(choice))
    return True


def maintain_db(choice):
    """
    'maintain_db' function drives the process
    toward the preserving or the resetting database.
    :param choice:
    :return:
    """
    update_status = True
    if choice == str(0):
        print("La base de donnée actuelle va être utilisée !!")
        update_status = False
    else:
        print("La base de donnée actuelle va être réinitilalisée !!")
    return update_status


def get_settings():
    """
    'get_settings' function provides all parameters
    from the external settings ini file.
    It returns a dict.
    :return:
    """
    the_options = opt.Settings()
    params = the_options.get_data_file_ini("loading")
    return params
