"""
Welcome to the main program.
When it starts the program process is following the steps below:
- Initialization with the "loading.py" module.
- Retrieving external parameters with the "options.py" module.
- Managing local database with the "mysql_operarions.py" module.
- Retrieving OpenfoodFacts server data with the "api_operations.py" module.
- Displaying and managing HMI - (Human Machine Interface) with the "console.py" module.
"""
# -*- coding: utf-8 -*-
import Packages.console as console


def main():
    """ Main program"""
    console.start_program()


if __name__ == "__main__":

    main()
