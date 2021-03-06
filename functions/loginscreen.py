#!/usr/bin/env  python3
"""
Create Login Screen.

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
from tkinter import Button
from tkinter import Entry
from tkinter import Label
from tkinter import PhotoImage
from tkinter import Tk


def data_user():
    """
    Funcion para guardar temporalmente los datos de usuario.

    Crea una archivo temporal que guardara las credenciales del usuario.
    """
    directory = getcwd()

    username = username_entry.get()
    password = password_entry.get()

    with open(file=f"{directory}/tmp/dtusp.txt", mode="w") as f:
        f.write(f"{username},{password}")
        f.close()

    logging.destroy()


def LoginScreen():
    """
    Funcion para crear una ventana de logeo.

    Crea una ventana de logeo que permite al usuario ingresar el usuario y
    el password para las conexiones remotas.
    """
    global logging
    global username_entry
    global password_entry

    directory = getcwd()

    logging = Tk()
    logging.geometry("275x350")
    logging.title("LOGIN ACCESS")
    logging.configure(background="white")

    image_file = PhotoImage(file=f"{directory}/images/lapiz.png")
    imagen_label = Label(logging, image=image_file, bg="white")
    imagen_label.place(x=65, y=170)

    Label(
        logging, text="Username:", bg="white",
        font=("Helvtica", 15)).grid(row=1, column=0)

    username_entry = Entry(
            logging, bg="white",
            font=("Helvtica", 15))
    username_entry.grid(row=2, column=0)

    Label(
        logging, text="Password:", bg="white",
        font=("Helvtica", 15)).grid(row=3, column=0)

    password_entry = Entry(
            logging, bg="white",
            font=("Helvtica", 15), show='???')
    password_entry.grid(row=4, column=0)

    Button(
        logging, command=data_user,
        text="Login", font=("Helvtica", 15)).grid(
            row=5, column=0
            )

    logging.mainloop()
