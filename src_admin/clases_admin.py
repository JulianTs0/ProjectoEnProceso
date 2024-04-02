from database_admin import *

#   Clase Usuario, usada para crear objetos tipo Usuario y tenes mas comodamente los 3 campos que contiene

class Admin:
    def __init__(self, name, password):

        self.name = name
        self.password = password

class Usuario:
    def __init__(self, name, email):

        self.name = name
        self.email = email

class Parametro:
    def __init__(self, name, price):

        self.name = name
        self.price = price
