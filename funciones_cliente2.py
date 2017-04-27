#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import ast

def imprimir(cadena):
    lista = json.loads(cadena)
    for i in lista:
        #print i
        print ast.literal_eval(json.dumps(i))

def iniciar_sesion():
    pass