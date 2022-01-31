#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
This script is reboot IPv4 phones.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
__author__ = "Cesar Rodriguez"
__copyright__ = "Copyright 2020"
__credits__ = ["Cesar Rodriguez"]
__license__ = "GPL"
__version__ = "1.0.2"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesarrodriguezpadilla@gmail.com"
__status__ = "Development"


# Import functions
from json import load
from json import dumps
from json import JSONDecodeError
from os import getcwd


# Colores para impresion en pantalla.
color_reset = "\x1b[0m"
red = "\x1b[00;00;1;031m"
red_blink = "\x1b[00;00;05;031m"
magent = "\x1b[00;00;02;033m"
magent_blink = "\x1b[00;00;05;033m"
blue = "\x1b[00;00;1;034m"
blue_blink = "\x1b[00;00;5;034m"
green = "\x1b[00;00;01;092m"
green_blink = "\x1b[00;00;5;092m"


def JSONDataImport():
    """
    Funcion importa el archivo sucursales.

    Funcion que importa el archivo *.json de la carpeta "sucursales".
    """
    try:
        # Find work directory
        directory = getcwd()

        file = f"{directory}/branches/branches.json"

        # Import file
        with open(file=file, mode="r") as f:
            data_json = load(f)

        return data_json

    except JSONDecodeError as error:
        print(f" {red}El archivo {green}{file} {red}contiene errores")
        error = str(error).split(" ")
        error_expection = (
            f" {blue}{error[0]} {error[1]} {red}{error[2]} {green}{error[3]}" +
            f" {red}{error[4]} {green}{error[5]} {blue}{error[6]} {error[7]}")
        print(f"{error_expection}")
        print(f" {green}Aqui un ejemplo.\n")

        # Open example.json file and read
        file = f"{directory}/branches/example.json"
        with open(file=file, mode="r") as f:
            data_json = load(f)

        print(dumps(data_json, indent=4))

        return False

    except FileNotFoundError:
        print(f" {red}El archivo {green}{file} {red} no se encuentra")
        print(f" {red}Revisa extension, lugar o que el archivo exista.")

        return False
