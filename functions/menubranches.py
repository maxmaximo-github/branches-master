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


# Import Functions


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


def MenuBranches(branches):
    """
    Funcion para la creacion de la estrutura de datos.

    Esta funcion realiza la estructura de datos a partir de archivos
    guardados en la carpeta sucursales.

    Al terminar se regresa "devices_list" para su posterior tratamiento.
    """
    print(f" {green}{'='*75}{color_reset}")
    print(
        f"{' '*4}{red}{'SUCURSALES':^20} " +
        f"  {blue}{'PREFIJOS IPv4':^20}   {'PREFIJOS IPv6':^20}{color_reset}")
    print(f" {green}{'='*75}{color_reset}")

    count = 0
    for branch in branches["Branches"]:
        ipv4_network = (
            f"{branch['Prefixs']['IPv4']}/{branch['Prefixs']['IPv4_len']}")
        ipv6_network = (
            f"{branch['Prefixs']['IPv6']}/{branch['Prefixs']['IPv6_len']}")
        print(
            f"  {yellow}{count}) {red}{branch['Name']:^20} {green}==>"
            + f"{blue}{ipv4_network:^20}   {ipv6_network:^20}")
        count += 1
    print(
        f"  {yellow}{'-'}) {red}{'Todas':^20} {green}==>"
        + f" {blue}{'*':^20}{color_reset}")
    print(f" {green}{'='*75}{color_reset}\n")
    print(
        f" {red}Si deseas {blue}testear {red}varias sucursales separa por "
        + f"{blue}coma {green}','{color_reset}")
    print(f"\t{blue}Example:{green} 0, 3, 5{color_reset}\n")
    print(
        f" {red}Si deseas un {blue}rango {red}utiliza {green}'-'{color_reset}")
    print(f"\t{blue}Example:{green} 1-3, 5{color_reset}\n")
    print(f" {red}Para {blue}Todas {red}las sucursales {green}'Inicial-Final'")
    print(f"\t{blue}Example: {green}0-{count-1}\n")


def MenuBranches2(branches):
    """
    Funcion para la creacion de la estrutura de datos.

    Esta funcion realiza la estructura de datos a partir de archivos
    guardados en la carpeta sucursales.

    Al terminar se regresa "devices_list" para su posterior tratamiento.
    """
    print(f" {green}{'='*25}{color_reset}")
    print(f"{' '*4}{red}{'SUCURSALES':^20} ")
    print(f" {green}{'='*25}{color_reset}")

    count = 0
    for branch in branches["Branches"]:
        print(f" {yellow}{count}) {red}{branch['Name']:^20}")
        count += 1
    print(
        f" {yellow}{'-'}) {red}{'Todas':^20}"
        + f"{color_reset}")
    print(f" {green}{'='*25}{color_reset}\n")

    print(
        f" {red}Si deseas {blue}testear {red}varias sucursales separa por "
        + f"{blue}coma {green}','{color_reset}")
    print(f"\t{blue}Example:{green} 0, 3, 5{color_reset}\n")
    print(
        f" {red}Si deseas un {blue}rango {red}utiliza {green}'-'{color_reset}")
    print(f"\t{blue}Example:{green} 1-3, 5{color_reset}\n")
    print(f" {red}Para {blue}Todas {red}las sucursales {green}'Inicial-Final'")
    print(f"\t{blue}Example: {green}0-{count-1}\n")
