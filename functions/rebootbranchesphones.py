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
# from functions.branchesfortest import BranchesForPing
from functions.branchesfortest import BranchesForRestart
from functions.clearscreen import ClearScreen
from functions.createbrancheslist import CreateBranchesList
from functions.countdown import CountDown
from functions.loginscreen import LoginScreen
from functions.menubranches import MenuBranches
from functions.pingpong import PingPongPhone
from functions.readdata import ReadData
from functions.readfiles import ReadFiles
from functions.removefiles import RemoveFiles
from functions.restartphone import RestartPhone
from functions.sshalive import SSHAlive
from functions.threadconfig import ThreadConfig
from functions.threadconfig import ThreadConfigSSH
from functions.threadconfig import ThreadConfigParamiko


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


def RebootBranchesPhones(branches):
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

        dictionary_prefix = BranchesForRestart(
                                branches, branches_inputlist)

        # Pedir contrasena para los telefonos
        LoginScreen()
        data_info = ReadData()
        RemoveFiles()

        for index in dictionary_prefix:
            dictionary_sucursal = index

            for (key, value) in dictionary_sucursal.items():

                # Impresion de formato para la terminal
                print(f" {green}{'='*66}{color_reset}\n")
                print(
                    f"\t {blue}Conectando {red}con la sucursal "
                    + f"{green}'{key}'\n")
                print(f"{red}{'*'*55:^66}{color_reset} ")
                print(
                    f"      {blue}Realizando {green}PING "
                    + f"{blue}a los {red}Telefonos de"
                    + f" {green}'{key}' {color_reset}\n")
                # Llamada a la funcion "thread_config" para la creacion de los
                # hilos y determinar que dispositivos son alcanzados por
                # ping
                ThreadConfig(PingPongPhone, value)
                # Impresion de formato para la terminal.
                print(f"{red}{'*'*55:^66}{color_reset} ")

                # Leer los archivos de los dispositivos que se encuentran
                # activos.
                devices_ssh = ReadFiles()

                # Remover archivos temporales con las IP
                RemoveFiles()

                # Impresion de formato para la terminal
                print(f"\n{red}{'*'*55:^66}{color_reset} ")
                print(
                    f"\t{blue} Probando {red}conectividad "
                    + f"{green}SSH {red}con {green}'{key}' {color_reset}\n")

                # Llamada a la funcion "thread_config" para la creacion de los
                # hilos y determinar que dispositivos son alcanzados por SSH
                ThreadConfigSSH(SSHAlive, devices_ssh, data_info)

                # Impresion de formato para la terminal
                print(f"{red}{'*'*55:^66}{color_reset} ")

                # Leer los archivos de los dispositivos que se encuentran
                # activos SSH.
                devices_configuration = ReadFiles()

                # Impresion de formato para la terminal
                print(f"\n{red}{'*'*55:^66}{color_reset} ")
                print(
                    f"\t\t{blue} Reiniciando Telefonos "
                    + f"{green}'{key}'{color_reset}")

                # Llamada a la funcion "thread_config" para la creacion de los
                # hilos y determinar que dispositivos son alcanzados por SSH
                ThreadConfigParamiko(
                    RestartPhone, devices_configuration, data_info)
                # Impresion de formato para la terminal
                print(f"{red}{'*'*55:^66}{color_reset} ")
                print(f" {green}{'='*66}{color_reset}\n\n\n")

                # Limpiar archivos de la carpeta temporal para la siguiente
                # ejecution.
                RemoveFiles()

        # Impresion de formato para la terminal.
        print(f" {green}{'='*66}")
        print(
            f"  {red}Esperando {green}reinicio {red}para comprobar"
            + f" la {green}conectividad {red}con "
            + f"{green}Telefonos.{magent_blink}")

        # Llamada a la funcion count_down y pasarle argumentos con valores
        # de ejemplo minutos=2 y segundo=0
        CountDown(minutes=0, seconds=20)

        # Impresion de formato para la terminal.
        print(f" {green}{'='*66}\n\n\n")

        # Realizar ping nuevamente para determinar que los telefonos
        # Ya son disponibles
        for index in dictionary_prefix:
            dictionary_sucursal = index

            for (key, value) in dictionary_sucursal.items():

                print(f" {green}{'='*66}{color_reset}\n")
                print(
                    f"\t {blue}Conectando {red}con la sucursal "
                    + f"{green}'{key}'\n")
                print(f"{red}{'*'*55:^66}{color_reset} ")
                print(
                    f"      {blue}Realizando {green}PING "
                    + f"{blue}a los {red}Telefonos de"
                    + f" {green}'{key}' {color_reset}\n")

                # Llamada a la funcion "thread_config" para la creacion de los
                # hilos y determinar que dispositivos son alcanzados por
                # ping
                ThreadConfig(PingPongPhone, value)

                # Impresion de formato para la terminal.
                print(f"{red}{'*'*55:^66}{color_reset} ")
                print(f" {green}{'='*66}{color_reset}")

                # Limpiar archivos de la carpeta temporal para la siguiente
                # ejecution.
                RemoveFiles()

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
