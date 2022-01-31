#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
Read Data Info.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
__author__ = "Cesar Rodriguez"
__copyright__ = "Copyright 2020"
__credits__ = ["Cesar Rodriguez"]
__license__ = "GPL"
__version__ = "0.5.0"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesarrodriguezpadilla@gmail.com"
__status__ = "Development"


# Import functions
from os import getcwd


def ReadData():
    """
    Funcion para leer archivos temporales.

    Se lee el archivo temporal que contiene las credenciales del usuario.
    """
    directory = getcwd()

    for line in open(file=f"{directory}/tmp/dtusp.txt", mode="r"):
        data_info = line.strip("\n").split(",")

    return data_info
