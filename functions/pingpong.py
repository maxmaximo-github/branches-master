#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
This script is create for ping IPv4.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
__author__ = "Cesar Rodriguez"
__copyright__ = "Copyright 2020, Reboot IPv4 Phones"
__credits__ = ["Cesar Rodriguez"]
__license__ = "GPL"
__version__ = "1.0.2"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesarrodriguez@gmail.com"
__status__ = "Development"


# Import Functions
from ipaddress import ip_address
from os import getcwd
from os import name
from os import popen
from subprocess import call
from subprocess import STDOUT
# Own Functions
from functions.ipversion import IPTypeVersion


# Colores para impresion de pantalla.
color_reset = "\x1b[0m"
red = "\x1b[00;00;1;031m"
red_blink = "\x1b[00;00;5;031m"
magent = "\x1b[00;00;02;033m"
magent_blink = "\x1b[00;00;02;033m"
blue = "\x1b[00;00;1;034m"
blue_blink = "\x1b[00;00;5;034m"
green = "\x1b[00;00;01;092m"
green_blink = "\x1b[00;00;5;092m"


def PingPong(values_ips):
    """
    Funcion para testear IPv4.

    Esta funcion realiza el testeo de Ping.

    Si el resultado es exitoso se guarda en un archivo de texto, de no ser asi
    sino solo se anuncia que no tiene conectividad.
    """
    try:
        name_device, ip, type = values_ips

        ip_address(ip)

        # Check what is the ip version.
        version = IPTypeVersion(ip)

        # Obtener la ruta actual del proyecto.
        directory = getcwd()
        file = f"{directory}/tmp/{name_device}_{ip}.txt"

        if name == "nt":
            reply = popen(f"ping {ip} -n 4").read()

            if "Received = 4" and "Approximate" in reply:
                print(
                    f" {red}El {blue}{type} {green}{name_device} " +
                    f"{red}con la {blue}IPv{version} {green}{ip} " +
                    f"{red}esta vivo." +
                    f"{blue}({red}Ping Success!!!!{blue}){color_reset}")

                # Crear un archivo en la carpeta tmp/nombre_device+ip
                with open(file=file, mode="w") as f:
                    f.write(f"{ip}")
                    f.close()

            else:
                print(
                    f" {red_blink}El {blue_blink}{type} {green}{name_device}" +
                    f" {red}con la {blue}IPv{version} {green}{ip} " +
                    f"{red_blink}no esta disponible. " +
                    f"{blue}({green}Ping Fail!!!!{blue}){color_reset}")

        else:
            reply = call(
                f"ping -c 3 {ip}",
                shell=True,
                stdout=open('/dev/null', 'w'),
                stderr=STDOUT
                )

            if reply == 0:
                print(
                    f" {red}El {blue}{type} {green}{name_device} " +
                    f"{red}con la {blue}IPv{version} {green}{ip} " +
                    f"{red}esta vivo." +
                    f"{blue}({red}Ping Success!!!!{blue}){color_reset}")
                # Crear un archivo en la carpeta tmp/nombre_device+ip
                with open(file=file, mode="w") as f:
                    f.write(f"{ip}")
                    f.close()

            else:
                print(
                    f" {red_blink}El {blue_blink}{type} {green}{name_device}" +
                    f" {red}con la {blue}IPv{version} {green}{ip} " +
                    f"{red_blink}no esta disponible. " +
                    f"{blue}({green}Ping Fail!!!!{blue}){color_reset}")

    except ValueError:
        print(f" \t{blue}{'='*66}")
        print(f"  \t{red_blink}    {('Error '*10):^40}")
        print(
            f" \t{blue}'NO SE PUEDE REALIZAR PING' {green}a " +
            f"{red}{name_device} {green}porque" +
            f" no tiene una {red}IPv4{green}/{red}IPv6 {green}valida.")
        print(f" \t{blue}{'='*66}")


def PingPongPhone(ip):
    """
    Funcion para testear IPv4.

    Esta funcion realiza el testeo de Ping.

    Si el resultado es exitoso se guarda en un archivo de texto, de no ser asi
    sino solo se anuncia que no tiene conectividad.
    """
    if name == "nt":
        reply = popen(f"ping {ip} -n 4").read()

        if "Received = 4" and "Approximate" in reply:
            print(
                f"    {red}El Telefono {green}IPv4 {blue}{ip} {red}esta vivo. "
                + f"{blue}({green_blink}Ping Success!!!!{blue}){color_reset}")

            directory = getcwd()
            f = open(file=f"{directory}/tmp/{ip}", mode="w")
            f.write(f"{ip}")
            f.close()

    else:
        reply = call(
            f"ping -c 3 {ip}",
            shell=True,
            stdout=open('/dev/null', 'w'),
            stderr=STDOUT)

        if reply == 0:
            print(
                f"    {red}El Telefono {green}IPv4 {blue}{ip} {red}esta vivo. "
                + f"{blue}({green_blink}Ping Success!!!!{blue}){color_reset}")

            directory = getcwd()
            f = open(file=f"{directory}/tmp/{ip}", mode="w")
            f.write(f"{ip}")
            f.close()
