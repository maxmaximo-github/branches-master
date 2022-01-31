#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
This script is remove files from tmp folder.

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
from glob import glob
from os import remove
from os import getcwd


def RemoveFiles():
    """
    Funcion para eliminar archivos de la carpeta tmp.

    Remueve los archivos que se generan temporalmente de la carpeta tmp
    """
    directory = getcwd()
    for file_name in glob(("{}/tmp/*").format(directory)):
        remove(file_name)
