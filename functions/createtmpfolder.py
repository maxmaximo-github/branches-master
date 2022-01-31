#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
This script is create a empty folder with name "tmp".

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
from os import mkdir
from os import path


def CreateTMPFolder():
    """
    Funcion para verificar si existe la carpeta tmp.

    Verificar si existe la carpeta tmp, en caso de no existir se creara
    para guardar los archivos temporales del proyecto.
    """
    # Obtener la ruta actual del proyecto.
    directory = getcwd()

    # Verificar si la carpeta tmp no existe.
    # Si no existe entra en la condicion, sino es ignorada.
    if not path.isdir(f"{directory}/tmp"):
        # Se crea la carpeta tmp dentro de la ruta del proyecto.
        mkdir(f"{directory}/tmp")
