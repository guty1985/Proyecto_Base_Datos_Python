#!/usr/bin/python
# -*- coding: utf-8 -*-

from socket import socket
import funciones_cliente2
from easygui import passwordbox

def main():
    server= socket()
    server.connect(('localhost', 80))
    dato = True
    a=0
    mensaje =True
    l= True
    while l == True:
        #enviar mensaje del cliente
        if mensaje == True:
            print "***BIENVENIDO A APUESTAS AZAR (GANE SU RED) ***"
            print "Ingrese su correo y presione enter >>"
            mensaje = False
        if dato == True:
            mensaje_cliente = raw_input("Ingrese Mensaje al Servidor >> ")
            if a == 0:
                dato = False
            else:
                pass
        else:
            mensaje_cliente = passwordbox("Ingrese Mensaje al Servidor >> ")
            dato = True
            a =1

        if mensaje_cliente:
            try:
                server.send(mensaje_cliente)
            except TypeError:
                server.send(bytes(mensaje_cliente, 'utf-8'))

        #respuesta servidor

        #mensaje_servidor = server.recv(1024)
        #if mensaje_servidor:
         #   print mensaje_servidor

        mensaje_servidor = server.recv(1024)
        if mensaje_servidor == "salir":
            l=False
            print "Gracias por utilizar nuestros servicios"
            server.close()
        else:
            funciones_cliente2.imprimir(mensaje_servidor)

if __name__ == '__main__':
    main()






