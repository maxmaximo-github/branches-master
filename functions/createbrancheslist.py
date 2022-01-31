#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
This script is create for general propouse.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
__author__ = "Cesar Rodriguez"
__copyright__ = "Copyright 2020"
__credits__ = ["Cesar Rodriguez"]
__license__ = "GPL"
__version__ = "1.5.2"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesarrodriguezpadilla@gmail.com"
__status__ = "Development"


# Import Functions
from functions.clearscreen import ClearScreen


# Colores para impresion en pantalla.
color_reset = "\x1b[0m"
red = "\x1b[00;00;1;031m"
red_blink = "\x1b[00;00;5;031m"
magent = "\x1b[00;00;02;033m"
magent_blink = "\x1b[00;00;02;033m"
blue = "\x1b[00;00;1;034m"
blue_blink = "\x1b[00;00;5;034m"
green = "\x1b[00;00;01;092m"
green_blink = "\x1b[00;00;5;092m"


def CreateBranchesList():
    """
    Funcion para introducir las sucursales.

    Esta funcion permite definir la lista de sucursales que se realizara
    el test.
    """
    try:
        # Usuario ingresa los valores de las sucursales_list
        print(f" {green}{'='*75}")
        sucursales_input = input(
            f" {red}Ingresa {green}No. {blue}de las "
            + f"{red}sucursales {blue}>> {green}")

        # Dividir el ingreso del usuario en comas
        sucursales_input = sucursales_input.split(",")

        # Lista vacia para obtener para la manipulacion de 'sucursales_input'
        tmp_sucursaleslist = []
        # Ciclo for para creacion de lista de sucursales
        for no_sucursal in sucursales_input:
            # Si se agrega un rango Ex: 1-3 se entra en esta condicion
            if "-" in no_sucursal:
                # Division de numeros.
                datos_test = no_sucursal.split("-")

                # Lista vacia de datos
                datos = []
                for _ in datos_test:
                    _ = int(_)
                    datos.append(_)

                # Permitir que se ingrese datos a la inversa Ex: 50-25
                if datos[0] > datos[-1]:
                    datos[0], datos[-1] = datos[-1], datos[0]

                # Creacion de las condiciones del ciclo for
                start = datos[0]
                finish = datos[-1] + 1
                # Creacion de una un rango #Example 1-5 a
                # 1, 2, 3, 4, 5
                for _ in range(start, finish, 1):
                    tmp_sucursaleslist.append(_)

            elif ", " in no_sucursal:
                no_sucursal = no_sucursal.split(",")
                no_sucursal = no_sucursal.strip(" ")
                no_sucursal = int(no_sucursal)
                tmp_sucursaleslist.append(no_sucursal)

            elif " " in no_sucursal:
                no_sucursal = no_sucursal.strip(" ")
                no_sucursal = int(no_sucursal)
                tmp_sucursaleslist.append(no_sucursal)

            elif no_sucursal.isnumeric():
                no_sucursal = int(no_sucursal)
                tmp_sucursaleslist.append(no_sucursal)

            else:
                no_sucursal = int(no_sucursal)
                tmp_sucursaleslist.append(no_sucursal)

        # Lista vacia para guardar los valores de las sucursales introducidas
        sucursales_list = []
        # Recorrido de sucursales para determinar si existe alguna repedita
        for sucursal_norepetida in tmp_sucursaleslist:
            # Si se encuentra una sucursal repetida sera omitida y no se
            # agregara a sucursales_list
            if sucursal_norepetida not in sucursales_list:
                sucursales_list.append(sucursal_norepetida)

        # Ordenar la lista
        sucursales_list.sort()

    except ValueError:
        ClearScreen()

        # Lista vacia para agregar valores no permitidos
        error = []
        # Ciclo for para determinar que valores no estan permitidos
        for valor in sucursales_input:
            if " " in valor:
                valor = valor.strip(" ")

            if not valor.isnumeric():
                error.append(valor)

        print(f" {blue}{'='*66}")
        print(f"  {red_blink} {('Error '*10):^40}")
        print(f" {blue}{'='*66}\n")
        print(
            f" {red}El programa {green}NO PUEDE CONTINUAR"
            + f" {red}debido a lo siguiente:{color_reset} \n")
        print(f" {red}Posiblemente ingresaste {green}'DATOS NO VALIDOS'.\n")
        print(f" {red}Tus datos que causan error son: ")
        print(f"     {green}{error}{color_reset}\n")

    except KeyboardInterrupt:
        print(
            f"\n\n{red}Has detenido el {green}programa {red}con el teclado.")

    return sucursales_list
