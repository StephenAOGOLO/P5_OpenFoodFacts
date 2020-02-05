"""
Welcome to the loading module, 'loading.py'.
This module is especially composed of one function.
Which is used to initialize and feeds program parameters.
"""
# -*- coding: utf-8 -*-
import configparser
import os
import time
import psutil
import logging as lg
lg.basicConfig(level=lg.WARNING)


def initialization():
    """
    So this function is ran to concentrate these parameters first and return dict ready to use.
    """
    os.system(".\\Packages\\root_link.bat")
    root_status = False
    while 1:
        process_report = find_process("mysql.exe")
        print(process_report)
        if process_report[1]:
            print("vrai")
        else:
            print("faux")
            root_status = True
            break
    return root_status
        #for key, value, in process_report[0].items():
            #print(key, value["nom"])
            #print(process_report[1])



        #if value["nom"] in process_report[0].values():
        #    break
    #for i in range(1,11):
    #    print("Vous avez {} secondes pour vous authentifier en tant que root".format(11-i))
    #    time.sleep(1)
    #os.system(".\\Packages\\root_link.bat")


def find_process(the_process="le_program_executable.exe"):
    dico_processus = {}
    status = False
    for indice, process in enumerate(psutil.process_iter()):
        if process.name() == the_process:
            lg.info("Voici le/les processus %s en cours d'execution", the_process)
            lg.info("%s", process)
            dico_processus[str(indice)] = {}
            dico_processus[str(indice)]["nom"] = process.name()
            dico_processus[str(indice)]["pid"] = process.pid
            dico_processus[str(indice)]["complete_info"] = process
            status = True
        else:
            lg.info("le/les processus %s est/sont introuvable(s)", the_process)
            pass
    return dico_processus, status


if __name__=="__main__":
    initialization()


