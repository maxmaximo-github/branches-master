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
__version__ = "1.0.0"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesarrodriguez@gmail.com"
__status__ = "Development"


# Import functions
# Import Own Functions
from functions.branchesfortest import BranchesForPing
from functions.clearscreen import ClearScreen
from functions.createbrancheslist import CreateBranchesList
from functions.loginscreen import LoginScreen
from functions.menubranches import MenuBranches
from functions.packetlatency import packetLatency
from functions.readdata import ReadData
from functions.removefiles import RemoveFiles
from functions.threadconfig import ThreadConfigSSH


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


def RestartPasswords(branches):
    """
    Funcion Principal.

    Esta funcion llama a las demas funciones de la carpeta 'functions'.

    Si el resultado es exitoso se guarda en un archivo de texto, de no ser asi
    sino solo se anuncia que no tiene conectividad.
    """
    try:
        # Limpiar pantalla
        ClearScreen()

        MenuBranches(branches)

        branches_inputlist = CreateBranchesList()

        devicesin_branches = BranchesForPing(
                                    branches,
                                    branches_inputlist)

        # Pedir contrasena para los telefonos
        LoginScreen()
        data_info = ReadData()
        RemoveFiles()

        for devices_item in devicesin_branches:
            print(f"{blue}{'='*80}{color_reset}")
            # print(f"{magent}Branche {devices_item.get()}")

            firewall_ips = []
            for name, values_ips in devices_item.items():
                print(f"{blue}Firewall {green}{name}.{color_reset}")

                for value in values_ips:
                    if "Firewall" in value[-1]:
                        firewall_ips.append(value[-2])

            ThreadConfigSSH(packetLatency, firewall_ips, data_info)

            print(f"{blue}{'='*80}{color_reset}")

        confirmation = input(
                f" {green}Deseas intentar" +
                f" nuevamente {green}Y{red}/{green}n {red}>> {green}")

        if confirmation.lower() in ["y", "ye", "yes"]:
            return True
        else:
            return False

    except KeyboardInterrupt:
        print(
            f"\n\n\t{red}Has detenido el {green}programa {red}con el teclado.")
