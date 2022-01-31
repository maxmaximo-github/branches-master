#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
This script is for configuration Ping Alive.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
__author__ = "Cesar Rodriguez"
__copyright__ = "Copyright 2020"
__credits__ = ["Cesar Rodriguez"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesarrodriguezpadilla@gmail.com"
__status__ = "Development"


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


def InputOption():
    """
    Funcion es para crear la ventana de logeo.

    Crea una ventana que permite poner las credenciales de los dispositivos
    de capa 2 y 3.
    """
    try:
        while True:
            input_user = input(f" {green}Inserta un valor {red}>> {green}")

            # Check if 'input_user' is a number
            if input_user.isnumeric():
                input_user = int(input_user)

                if input_user in [1, 2, 3]:
                    break

                else:
                    print(
                        f" \t{red}{input_user}{green}) {red}Opcion "
                        + f"{green}No Valida.{color_reset}\n")
                    # pass
                    continue

            else:
                print(
                    f" {blue}Has ingresado: {red}\"{green}{input_user}{red}\"")
                print(f" {blue}Opcion {red}\"{green}No Valida{red}\"")
                input_user = input(
                        f" {green}Deseas intentar" +
                        f" nuevamente {green}Y{red}/{green}n {red}>> {green}")

                if input_user.lower() in ["yes", "y", "ye"]:
                    continue
                else:
                    break

    except KeyboardInterrupt:
        print(
            f"\n\n\t{red}Has detenido el {green}programa {red}con el teclado.")

    return input_user
