#!/usr/bin/env  python3
"""
This script is create for ping IPv4.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
__author__ = "Cesar Alonso Salvador Rodriguez Padilla"
__copyright__ = "LLDP Relationships"
__credits__ = ["Cesar Rodriguez"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesar.ropadilla@alumnos.udg.mx"
__status__ = "Development"


from logging import basicConfig
from logging import DEBUG
from logging import getLogger

from netmiko import Netmiko
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException


basicConfig(filename="logs.log", level=DEBUG)
logger = getLogger("netmiko")


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


def packetLatency(ip, data_info):
    """
    Funcion para realizar configuracion default.

    Realiza multiples conexiones creando hilos para dicha tarea.
    Para quitar los mensajes de los demas.

    """
    username, password = data_info

    remote_device = {
        "ip": ip,
        "device_type": "autodetect",
        "username": username,
        "password": password
    }

    try:

        connection = Netmiko(**remote_device)

        connection.enable()

        lines = connection.send_command(
            "diagnose sys sdwan health-check").splitlines()

        links_up, links_down = [], []
        for line in lines:
            if "state(alive)" in line:

                line = line.replace("(", " ").replace(")", " ").replace(
                    ":", "").replace("Seq", "").replace(",", "").replace(
                    "sla_map=0x1", "").replace("sla_map=0x0", "")

                links_up.append(line)

            elif "state(dead)" in line:
                line = line.replace("(", " ").replace(")", " ").replace(
                    ":", "").replace("Seq", "").replace(
                    ",", "").replace("sla_map=0x0", "")
                links_down.append(line)

            else:
                continue

        for link in links_up:
            print(f"{green}{link}{color_reset}")

        for link in links_down:
            print(f"{red_blink}{link}{color_reset}")

        connection.disconnect()

    except NetMikoTimeoutException:
        print(f"{red}No se encuentra el dispositivo.")

    except NetMikoTimeoutException:
        print(f"Device {ip} not found.")

    except NetMikoAuthenticationException:
        print(f"Wrong credentials in {ip}.")

    except SSHException:
        print(f"Channel Closed in {ip}")

    except KeyboardInterrupt:
        print("You canceled the operation with the keyboard")

    except EOFError:
        print("Other error.")
