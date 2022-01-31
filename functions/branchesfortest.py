#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
This script is create for ping IPv4 devices..

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
__author__ = "Cesar Rodriguez"
__copyright__ = "Copyright 2020, Ping IPv4 Branche Offices Devices"
__credits__ = ["Cesar Rodriguez"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesarrodriguez@gmail.com"
__status__ = "Development"


# Own functions
from functions.clearscreen import ClearScreen


# Colores para impresion en pantalla.
color_reset = "\x1b[0m"
red = "\x1b[00;00;1;031m"
red_blink = "\x1b[00;00;05;031m"
magent = "\x1b[00;00;02;033m"
magent_blink = "\x1b[00;00;02;033m"
blue = "\x1b[00;00;1;034m"
blue_blink = "\x1b[00;00;5;034m"
green = "\x1b[00;00;01;092m"
green_blink = "\x1b[00;00;5;092m"
yellow = "\x1b[00;00;02;033m"


def BranchesForPing(branches, branches_inputlist):
    """
    Funcion para determinar que indices existen.

    Esta funcion determina que indices existen para realizar los pings
    correspondientes en las sucursales.
    """
    try:
        devices_list = []
        for branch in branches["Branches"]:
            branch_dic = {}
            name = branch["Name"]

            tmp_list = []
            for devices in branch["Devices"]:
                try:
                    device = [
                        devices["Name"],
                        devices["IPv4"],
                        devices["Type"]]
                    tmp_list.append(device)
                    branch_dic[name] = tmp_list

                except KeyError:
                    pass

                try:
                    device = [
                        devices["Name"],
                        devices["IPv6"],
                        devices["Type"]]
                    tmp_list.append(device)
                    branch_dic[name] = tmp_list

                except KeyError:
                    pass

            devices_list.append(branch_dic)

        branches_dictionary = []
        for branch in branches_inputlist:
            internal_dictionary = devices_list[branch]
            branches_dictionary.append(internal_dictionary)

    except IndexError:
        ClearScreen()

        branches_inexistentes = []
        for no_sucursal in branches_inputlist:
            if no_sucursal > len(devices_list)-1:
                branches_inexistentes.append(no_sucursal)

        print(f" {green}{'='*66}")
        print(f" {blue_blink} {('Precaucion '*6):^40}")
        print(f" {green}{'='*66}")
        print(
            f" {red}El programa {green}NO REALIZARA ACTIVIDAD"
            + f" {red}en las siguientes sucursales")
        print(f" {red}debido a lo siguiente:{color_reset} \n")
        print(f" {red}Las siguientes sucursales no existen: ")
        print(f" {green}{branches_inexistentes}{color_reset}\n")

    return branches_dictionary


def BranchesForRestart(branches, branches_inputlist):
    """
    Funcion para determinar que indices existen.

    Esta funcion determina que indices existen para realizar los pings
    correspondientes en las sucursales.
    """
    try:
        devices_list = []
        for branch in branches["Branches"]:
            name = branch["Name"]
            prefix_tmp = branch["Prefixs"]["IPv4"].split(".")
            prefix_tmp = ".".join(prefix_tmp[0:3])

            len_reboot = branch["RebootPhonesLen"].split("-")
            start = int(len_reboot[0])
            finish = int(len_reboot[-1]) + 1

            ip_list = []
            for ip in range(start, finish, 1):
                ip_list.append(f"{prefix_tmp}.{ip}")

            branch_dic = {
                name: ip_list
            }

            devices_list.append(branch_dic)

        branches_dictionary = []
        for branch in branches_inputlist:
            internal_dictionary = devices_list[branch]
            branches_dictionary.append(internal_dictionary)

    except IndexError:
        ClearScreen()

        branches_inexistentes = []
        for no_sucursal in branches_inputlist:
            if no_sucursal > len(devices_list)-1:
                branches_inexistentes.append(no_sucursal)

        print(f" {green}{'='*66}")
        print(f" {blue_blink} {('Precaucion '*6):^40}")
        print(f" {green}{'='*66}")
        print(
            f" {red}El programa {green}NO REALIZARA ACTIVIDAD"
            + f" {red}en las siguientes sucursales")
        print(f" {red}debido a lo siguiente:{color_reset} \n")
        print(f" {red}Las siguientes sucursales no existen: ")
        print(f" {green}{branches_inexistentes}{color_reset}\n")

    return branches_dictionary
