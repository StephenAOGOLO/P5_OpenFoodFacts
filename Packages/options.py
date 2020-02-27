"""
Welcome to the option module, 'options.py'.
This module is used to pick some parameters from an external file.
It contains four classes whose an abstract class and three concrete ones.
Each concrete class are called for the program initialization.
"""
# -*- coding: utf-8 -*-
import configparser as cp


class Settings:
    """
    This class manage data parameters stored in a external file.
    """
    def __init__(self):
        """
        This constructor create a instance which contains all the data from a file ini.
        """
        self.file_ini = ".\\Packages\\settings.ini"
        self.all_sections_file = self.get_all_sections_file_ini()

    def get_data_file_ini(self, section):
        """
        This method picks all data of a specified section from 'settings.ini'.


        :param section:
        :return data:
        """
        data = {}
        config = cp.RawConfigParser()
        config.read(self.file_ini)
        for j in config.options(section):
            data[str(j)] = str(config.get(section, j))
        return data

    def get_option_file_ini(self, section):
        """
        This method picks all options of a specified section from 'settings.ini'.

        :param section:
        :return config.options(section):
        """
        config = cp.RawConfigParser()
        config.read(self.file_ini)
        return config.options(section)

    def get_all_sections_file_ini(self):
        """
        This method picks all sections from 'settings.ini'.

        :return:
        """
        config = cp.RawConfigParser()
        config.read(self.file_ini)
        return config.sections()

    def get_particular_sections(self, pattern):
        """
        This method picks all options from a given section 'pattern'
        :param pattern:
        :return:
        """
        list_particular_section = []
        for section in self.all_sections_file:
            if pattern in section:
                list_particular_section.append(section)
        return list_particular_section
