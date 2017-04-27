#!/usr/bin/python
# -*- coding: utf-8 -*-

from socket import socket, error
from threading import Thread
import funciones_servidor2
import json


class Cliente(Thread):

    '''funcion que genera hilos'''
    def __init__(self, con, dire):
        Thread.__init__(self)
        self.conexion = con
        self.direccion= dire


    def run(self):
        l = True
        while l ==True:
            try:
                contrasena = False
                a=False
                b=False
                menu_1 = False
                while (a!= True):
                    while (b!=True):
                        mensaje_cliente=str(self.conexion.recv(1024))
                        comprador = mensaje_cliente

                        mensaje_cliente = funciones_servidor2.validar_usuario(mensaje_cliente)
                        usuario=mensaje_cliente

                        if usuario == True:
                                mensaje_cliente = funciones_servidor2.password()
                                self.conexion.send(mensaje_cliente)
                                mensaje_cliente = str(self.conexion.recv(1024))
                                operacion = mensaje_cliente
                                mensaje_cliente = funciones_servidor2.validar_contrasena(comprador,operacion,self.direccion)
                                contrasena = mensaje_cliente
                                b = True
                        else:
                            mensaje_cliente = funciones_servidor2.usuarios()
                            self.conexion.send(mensaje_cliente)
                            mensaje_cliente = str(self.conexion.recv(1024))
                            comprador = mensaje_cliente
                            b = True
                            contrasena = False
                    while (contrasena == True):

                        menu = False
                        while (menu != True):
                            mensaje_cliente=funciones_servidor2.menu_1()
                            self.conexion.send(mensaje_cliente)
                            mensaje_cliente = int(self.conexion.recv(1024))
                            operacion=mensaje_cliente
                            if operacion ==1 :
                                dato = 0
                                while dato < 2:
                                    mensaje_cliente = funciones_servidor2.menu_alertas()
                                    self.conexion.send(mensaje_cliente)
                                    dato = int(self.conexion.recv(1024))
                                    if dato == 1:
                                        mensaje_cliente = funciones_servidor2.maximo()
                                        self.conexion.send(mensaje_cliente)
                                    if dato == 2:
                                        pass
                            if operacion ==2:
                                dato =0
                                while dato <4:
                                    mensaje_cliente = funciones_servidor2.menu_loterias()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = int(self.conexion.recv(1024))
                                    dato = mensaje_cliente
                                    if  dato == 1:
                                        mensaje_cliente = funciones_servidor2.ver_loterias()
                                        self.conexion.send(mensaje_cliente)
                                    if  dato == 2:
                                        mensaje_cliente = funciones_servidor2.pedir_loteria()
                                        self.conexion.send(mensaje_cliente)
                                        mensaje_cliente = str(self.conexion.recv(1024))
                                        loteria = mensaje_cliente
                                        mensaje_cliente = funciones_servidor2.pedir_dia()
                                        self.conexion.send(mensaje_cliente)
                                        mensaje_cliente = str(self.conexion.recv(1024))
                                        dia = mensaje_cliente
                                        mensaje_cliente = funciones_servidor2.agregar_loteria(loteria,dia)
                                        self.conexion.send(mensaje_cliente)
                                    if dato == 3:
                                        #mensaje_cliente = funciones_servidor2.ver_loterias()
                                        #self.conexion.send(mensaje_cliente)
                                        mensaje_cliente = funciones_servidor2.pedir_loteria()
                                        self.conexion.send(mensaje_cliente)
                                        mensaje_cliente = str(self.conexion.recv(1024))
                                        num1 = mensaje_cliente
                                        mensaje_cliente = funciones_servidor2.pedir_dia()
                                        self.conexion.send(mensaje_cliente)
                                        mensaje_cliente = str(self.conexion.recv(1024))
                                        num2 = mensaje_cliente
                                        mensaje_cliente = funciones_servidor2.pedir_numero()
                                        self.conexion.send(mensaje_cliente)
                                        mensaje_cliente = int(self.conexion.recv(1024))
                                        num3 = mensaje_cliente
                                        mensaje_cliente = funciones_servidor2.actualizar_loteria(num1,num2,num3)
                                        self.conexion.send(mensaje_cliente)
                                    if dato == 4:
                                        pass

                            if operacion == 3:
                                dato = 0
                                while dato < 4:
                                    mensaje_cliente = funciones_servidor2.menu_ventas()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = int(self.conexion.recv(1024))
                                    dato = mensaje_cliente
                                    if  dato == 1:
                                        mensaje_cliente = funciones_servidor2.ver_chances()
                                        self.conexion.send(mensaje_cliente)

                                    if dato == 2:
                                        mensaje_cliente = funciones_servidor2.detalle_chances()
                                        self.conexion.send(mensaje_cliente)
                                    if dato == 3:
                                        mensaje_cliente = funciones_servidor2.pedir_fecha()
                                        self.conexion.send(mensaje_cliente)
                                        mensaje_cliente = str(self.conexion.recv(1024))
                                        fecha = mensaje_cliente
                                        mensaje_cliente = funciones_servidor2.chances(fecha)
                                        self.conexion.send(mensaje_cliente)
                                    if dato == 4:
                                        pass


                            if operacion == 4:
                                dato = 0
                                while dato < 4:
                                    mensaje_cliente = funciones_servidor2.menu_usuario()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = int(self.conexion.recv(1024))
                                    dato = mensaje_cliente
                                    if dato == 1:
                                        mensaje_cliente = funciones_servidor2.ver_usuarios()
                                        self.conexion.send(mensaje_cliente)
                                    if dato == 2:
                                        mensaje_cliente = funciones_servidor2.puntos()
                                        self.conexion.send(mensaje_cliente)
                                    if dato == 3:
                                        mensaje_cliente = funciones_servidor2.usuario()
                                        self.conexion.send(mensaje_cliente)
                                        mensaje_cliente = str(self.conexion.recv(1024))
                                        usuario = mensaje_cliente
                                        mensaje_cliente = funciones_servidor2.cedula()
                                        self.conexion.send(mensaje_cliente)
                                        mensaje_cliente = str(self.conexion.recv(1024))
                                        cedula = mensaje_cliente
                                        mensaje_cliente = funciones_servidor2.tipo()
                                        self.conexion.send(mensaje_cliente)
                                        mensaje_cliente = str(self.conexion.recv(1024))
                                        tipo = mensaje_cliente
                                        mensaje_cliente = funciones_servidor2.email()
                                        self.conexion.send(mensaje_cliente)
                                        mensaje_cliente = str(self.conexion.recv(1024))
                                        correo = mensaje_cliente
                                        mensaje_cliente = funciones_servidor2.contrasena()
                                        self.conexion.send(mensaje_cliente)
                                        mensaje_cliente = str(self.conexion.recv(1024))
                                        password = mensaje_cliente
                                        mensaje_cliente = funciones_servidor2.crear_usuario(cedula,usuario,tipo,correo,password)
                                        self.conexion.send(mensaje_cliente)
                                    if dato == 4:
                                        pass

                            if operacion == 5:
                                mensaje_cliente = funciones_servidor2.menu_log_usuario()
                                self.conexion.send(mensaje_cliente)
                                mensaje_cliente = int(self.conexion.recv(1024))
                                dato = mensaje_cliente
                                if dato == 1:
                                    mensaje_cliente = funciones_servidor2.reportes()
                                    self.conexion.send(mensaje_cliente)
                                    print a
                                    #self.conexion.send(mensaje_cliente)
                                    #a
                            if operacion == 6:
                                mensaje_cliente = funciones_servidor2.validar_aciertos()
                                self.conexion.send(mensaje_cliente)

                            if operacion == 7:
                                menu =True
                                contrasena = False
                                menu_1 = True
                                a= True


                    while (menu_1!= True):
                        mensaje_cliente = funciones_servidor2.menu_loteria()
                        self.conexion.send(mensaje_cliente)
                        mensaje_cliente = int(self.conexion.recv(1024))
                        operacion = mensaje_cliente

                        if operacion == 1:
                            dato = 0
                            while dato < 3:
                                mensaje_cliente = funciones_servidor2.menu_hacer_chance()
                                self.conexion.send(mensaje_cliente)
                                mensaje_cliente = int(self.conexion.recv(1024))
                                dato = mensaje_cliente

                                if dato == 1:
                                    mensaje_cliente = funciones_servidor2.numero_suerte()
                                    self.conexion.send(mensaje_cliente)
                                if dato == 2:
                                    mensaje_cliente = funciones_servidor2.pedir_chance()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = int(self.conexion.recv(1024))
                                    num1 = mensaje_cliente
                                    mensaje_cliente = funciones_servidor2.ver_loterias()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = funciones_servidor2.escoger_loteria()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = (self.conexion.recv(1024))
                                    num2 = mensaje_cliente
                                    mensaje_cliente = funciones_servidor2.pedir_dinero()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = int(self.conexion.recv(1024))
                                    num3 = mensaje_cliente
                                    mensaje_cliente = funciones_servidor2.pago_dinero()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = int(self.conexion.recv(1024))
                                    num4 = mensaje_cliente
                                    mensaje_cliente = funciones_servidor2.confirmar_pago()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente =str(self.conexion.recv(1024))
                                    pago = mensaje_cliente
                                    if pago =="S":
                                        mensaje_cliente = funciones_servidor2.generar_chance(num1, num2,num3,comprador,num4,num3)
                                        self.conexion.send(mensaje_cliente)
                                if dato == 3:
                                    pass

                        if operacion == 2:
                            dato = 0
                            while dato < 3:

                                mensaje_cliente = funciones_servidor2.menu_puntos()
                                self.conexion.send(mensaje_cliente)
                                mensaje_cliente = int(self.conexion.recv(1024))
                                dato = mensaje_cliente
                                if dato == 1:
                                    mensaje_cliente = funciones_servidor2.ver_puntos(comprador)
                                    self.conexion.send(mensaje_cliente)
                                if dato == 2:
                                    mensaje_cliente = funciones_servidor2.ver_productos()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = funciones_servidor2.pedir_producto()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = str(self.conexion.recv(1024))
                                    num4 = mensaje_cliente
                                    mensaje_cliente = funciones_servidor2.cambiar_producto(comprador,num4)
                                    self.conexion.send(mensaje_cliente)
                                if dato == 3:
                                    pass

                        if operacion == 3:
                            dato = 0
                            while dato < 3:

                                mensaje_cliente = funciones_servidor2.menu_chances()
                                self.conexion.send(mensaje_cliente)
                                mensaje_cliente = int(self.conexion.recv(1024))
                                dato = mensaje_cliente
                                if dato == 1:
                                    mensaje_cliente = funciones_servidor2.ver_chance(comprador)
                                    self.conexion.send(mensaje_cliente)
                                if dato == 2:
                                    mensaje_cliente = funciones_servidor2.detalle_chance(comprador)
                                    self.conexion.send(mensaje_cliente)
                                if dato == 3:
                                    pass

                        if operacion == 4:
                            mensaje_cliente = funciones_servidor2.pedir_chance()
                            self.conexion.send(mensaje_cliente)
                            mensaje_cliente = int(self.conexion.recv(1024))
                            n_chance = mensaje_cliente
                            mensaje_cliente = funciones_servidor2.pedir_fecha()
                            self.conexion.send(mensaje_cliente)
                            mensaje_cliente = str(self.conexion.recv(1024))
                            chance_fecha = mensaje_cliente
                            mensaje_cliente = funciones_servidor2.escoger_loteria()
                            self.conexion.send(mensaje_cliente)
                            mensaje_cliente = str(self.conexion.recv(1024))
                            loteria = mensaje_cliente
                            mensaje_cliente = funciones_servidor2.aciertos(n_chance,chance_fecha,loteria)
                            self.conexion.send(mensaje_cliente)

                        if operacion == 5:
                            contrasena = False
                            menu_1 = True
                            a = True
                            l = False
                            #mensaje_cliente = funciones_servidor2.adios()
                            #recibido = self.conexion.send(mensaje_cliente)
                            #self.conexion.send(recibido)


            except error:
                print("[%s] Error de lectura "%self.name)
                break
            else:
                if mensaje_cliente:
                    mensaje_cliente = funciones_servidor2.adios()
                    recibido = self.conexion.send(mensaje_cliente)
                    self.conexion.send(recibido)
def main():
    server = socket()
    server.bind(("localhost", 80))
    server.listen(1)


    while True:
        con, dire = server.accept()
        hilo= Cliente(con, dire)
        hilo.start()
        print("conexion de %s:%d " %dire)
        #hilo =Thread(target=funciones_servidor2.menu,args=())
        #hilo.start()

if __name__ == '__main__':
    main()

