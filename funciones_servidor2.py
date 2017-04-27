#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import json
import time
import os
import MySQLdb
import datetime

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = ''
DB_NAME = 'apuestas_azar'


def run_query(query=''):
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]

    conn = MySQLdb.connect(*datos)  # Conectar a la base de datos
    cursor = conn.cursor()  # Crear un cursor
    cursor.execute(query)  # Ejecutar una consulta

    if query.upper().startswith('SELECT'):
        data = cursor.fetchall()  # Traer los resultados de un select
    else:
        conn.commit()  # Hacer efectiva la escritura de datos
        data = None

    cursor.close()  # Cerrar el cursor
    conn.close()  # Cerrar la conexión

    return data


#Menus Usuario Cliente--------------------------------------------------------
def menu_loteria():
    lista = ["*****Apuestas Azar*****", "1. Hacer Chance", "2. Puntos",
             "3. Chances", "4. Comprobar Aciertos",
             "5. Salir", "Digite la opcion >>"]
    cadena = json.dumps(lista)
    return cadena

def menu_hacer_chance():
    lista = ["Hacer Chance", "1. Ver Numeros Suerte", "2. Realizar del Chance",
             "3. Salir", "Digite la opcion >>"]
    cadena = json.dumps(lista)
    return cadena

def menu_puntos():
    lista = ["Puntos", "1. Ver Puntos", "2. Cambiar Puntos * Productos",
             "3. Salir", "Digite la opcion >>"]
    cadena = json.dumps(lista)
    return cadena

def menu_chances():
    lista = ["Chances", "1. Ver listado Chances", "2. Detalle Chances",
             "3. Salir", "Digite la opcion >>"]
    cadena = json.dumps(lista)
    return cadena

#Funciones Usuario Cliente--------------------------------------------------------
def numero_suerte():
    lista = []
    for i in range(5):
        lista.append(random.randint(0000, 9999))

    cadena = json.dumps(lista)
    return cadena

def pedir_chance():
    lista = ["Ingrese Numero Chance y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def escoger_loteria():
    lista = ["Ingrese Loteria y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def pedir_dinero():
    lista = ["Ingrese Monto Realizar Chance y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def pago_dinero():
    lista = ["Ingrese Valor Denominacion Billete y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def confirmar_pago():
    lista = ["Confirmar Pago Chance (S/N) y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def generar_chance(chance,loteria,valor,comprador,dinero_cliente,valor_chance):
    fecha = datetime.date.today()
    hoy = fecha.strftime("%d/%m/%y")
    hora = time.strftime("%X")
    acierto = [[chance]]


    query = "INSERT INTO chance (nombre_comprador,numero_chance,loteria,valor,fecha,hora)VALUES('%s','%s','%s','%s','%s','%s')"%(comprador,chance,loteria ,valor,hoy,hora)
    run_query(query)

    puntos = valor/100

    query = "INSERT INTO puntos (nombre_persona,puntos) VALUES('%s','%s')"%(comprador,puntos)
    run_query(query)

    pago = valor * 5000

    query = "SELECT numero FROM loteria WHERE numero = '%s'" % chance
    result = run_query(query)
    cadena = json.dumps(result)

    if acierto == cadena:
        query = "INSERT INTO aciertos (nombre_ganador,loteria,numero_chance,valor_chance,fecha,pago_ganador)VALUES('%s','%s','%s','%s','%s','%s')" % (comprador, loteria, chance, valor, hoy, pago)
        run_query(query)

    resultado = dinero_cliente - valor_chance
    lista = ["Dinero Entregado $" + str(dinero_cliente) + '\n' +
             "Valor del Chance $" + str(valor_chance) + '\n' +
             "Devolucion Cliente $" + str(resultado) + '\n'+
             "Chance Creado Satisfactoriamente, Presione enter >>"]

    cadena = json.dumps(lista)
    return cadena

def ver_puntos(comprador):

    query = "SELECT nombre_persona, puntos FROM puntos WHERE nombre_persona = '%s'" % comprador
    result = run_query(query)

    cadena = json.dumps(result)
    return cadena

def ver_productos():

    query = "SELECT nombre_producto,puntos FROM productos"
    result = run_query(query)
    cadena = json.dumps(result)
    return cadena

def pedir_producto():
    lista = ["Ingrese Producto a Cambiar, Presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def cambiar_producto(comprador,producto):

    query = "SELECT puntos FROM puntos WHERE nombre_persona = '%s'" % comprador
    result = run_query(query)
    puntos = json.dumps(result)
    print puntos

    query = "SELECT puntos FROM productos WHERE nombre_producto = '%s'" % producto
    result = run_query(query)
    puntos_producto = json.dumps(result)
    print puntos_producto

    if puntos == puntos_producto:
        lista = ["Puntos Cambiados Exitosamente, Presione enter >>"]
    else:
        lista = ["No Posee los puntos necesarios para obtener el producto, Presione enter >>"]

    cadena = json.dumps(lista)
    return cadena

def ver_chance(comprador):
    query = "SELECT numero_chance, loteria FROM chance WHERE nombre_comprador = '%s'" % comprador
    result = run_query(query)
    cadena = json.dumps(result)
    return cadena

def detalle_chance(comprador):
    query = "SELECT nombre_comprador, numero_chance,loteria,valor,fecha,hora FROM chance WHERE nombre_comprador = '%s'" % comprador
    result = run_query(query)
    cadena = json.dumps(result)
    return cadena

def pedir_fecha():
    lista = ["Ingrese Fecha Chance y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena


def aciertos(numero,chance,loteria):
    fecha = datetime.datetime.strptime(chance, '%d/%m/%y')
    dia_loteria = fecha.strftime("%A")
    dia = convertir(dia_loteria)
    query = "SELECT nombre,numero FROM loteria  WHERE dia = '%s' and nombre = '%s' and numero = '%s' "%(dia,loteria,numero)
    result = run_query(query)
    base = json.dumps(result)

    lista=[[loteria,numero]]
    cadena = json.dumps(lista)

    if base == cadena:
        lista = ["Felicitaciones ha ganado el chance, Presione enter >>"]
    else:
        lista = ["Lo sentimos, sigue intentando, Presione enter >>"]

    cadena = json.dumps(lista)
    return cadena

#Menus Usuario Administrador----------------------------------------------------

def menu_1():
    lista = ["Apuestas Azar (Admin)", "1. Alertas", "2. Loterias",
             "3. Ventas", "4. Usuarios", "5. Log Usuarios",
             "6. Aciertos","7. Salir", "Digite la opcion >>"]
    cadena = json.dumps(lista)
    return cadena

def menu_alertas():
    lista = ["Alertas", "1. Monto Maximo", "2. Salir", "Digite la opcion >>"]
    cadena = json.dumps(lista)
    return cadena

def menu_loterias():
    lista = ["Loterias", "1. Listado Loterias", "2. Agregar Loteria",
             "3. Actualizar Loterias", "4. Salir", "Digite la opcion >>"]
    cadena = json.dumps(lista)
    return cadena

def menu_ventas():
    lista = ["Ventas", "1. Listado Chances", "2. Detalle Chance",
             "3. Ventas Dia", "4. Salir", "Digite la opcion >>"]
    cadena = json.dumps(lista)
    return cadena

def menu_usuario():
    lista = ["Usuarios", "1. Listado Usuario", "2. Usuarios Puntos",
             "3. Crear Usuario","4. Salir", "Digite la opcion >>"]
    cadena = json.dumps(lista)
    return cadena

def menu_log_usuario():
    lista = ["Log Usuario", "1. Reportes", "2. Salir", "Digite la opcion >>"]
    cadena = json.dumps(lista)
    return cadena


#Funciones Administrador------------------------------------------------------

def ver_loterias():
    dia_loteria = time.strftime("%A")
    dia= convertir(dia_loteria)

    query = "SELECT nombre FROM loteria WHERE dia = '%s'" % dia
    result = run_query(query)
    cadena = json.dumps(result)
    return cadena

def pedir_loteria():
    lista = ["Ingrese Loteria y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena


def pedir_dia():
    lista = ["Ingrese Dia Juega Loteria y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def nueva_loteria():
    lista = ["Ingrese Nuevo Nombre Loteria y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def agregar_loteria(loteria,dia):
    numero =int(1985)
    query = "INSERT INTO loteria (nombre,dia,numero) VALUES ('%s','%s','%s')" % (loteria,dia,numero)
    run_query(query)
    lista = ["Loteria Creada Satisfactoriamente, Presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def pedir_numero():
    lista = ["Ingrese Nuevo Numero de la Loteria, Presione enter >>"]
    cadena = json.dumps(lista)
    return cadena


def actualizar_loteria(nombre,dia,numero):

    query = "UPDATE loteria SET numero=%i WHERE nombre = '%s' and dia ='%s' "%(int(numero),nombre,dia)
    run_query(query)
    lista = ["Numero Atualizado Correctamente, Presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def ver_chances():
    query = "SELECT numero_chance, loteria FROM chance"
    result = run_query(query)
    cadena = json.dumps(result)
    return  cadena

def detalle_chances():
    query = "SELECT nombre_comprador, numero_chance,loteria,valor,fecha,hora FROM chance"
    result = run_query(query)
    cadena = json.dumps(result)
    return cadena

def pedir_fecha():
    lista = ["Ingrese fecha (d/m/a) ventas del dia y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def chances(fecha):
    query = "SELECT nombre_comprador, numero_chance,loteria,valor,fecha,hora  FROM chance WHERE fecha = '%s'" % fecha
    result = run_query(query)
    cadena = json.dumps(result)
    return cadena

def ver_usuarios():
    query = "SELECT nombre_usuario, tipo_usuario FROM usuarios"
    result = run_query(query)
    cadena = json.dumps(result)
    return cadena

def puntos():
    query = "SELECT nombre_persona,sum(puntos) FROM puntos GROUP BY nombre_persona "
    result = run_query(query)

    cadena = json.dumps(result)
    return cadena

def crear_usuario(cedula, usuario, tipo, correo,contrasena):
    fecha = datetime.date.today()
    hoy = fecha.strftime("%d/%m/%y")
    query = "INSERT INTO usuarios (cedula,nombre_usuario,tipo_usuario,email,contrasena,fecha_registro)VALUES('%s','%s','%s','%s','%s','%s')" % (cedula, usuario, tipo, correo,contrasena, hoy)
    run_query(query)

    lista = ["Usuario creado satisfactoriamente y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def usuario():
    lista = ["Ingrese Nombre Usuario y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def cedula():
    lista = ["Ingrese # Cedula y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def tipo():
    lista = ["Ingrese el tipo de usuario(admin/usuario) y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def email():
    lista = ["Ingrese correo y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def contrasena():
    lista = ["Ingrese contrasena y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def validar_aciertos():
    query = "SELECT * FROM aciertos"
    result = run_query(query)
    cadena = json.dumps(result)
    return cadena


def usuarios():
    lista = ["Ingrese usuario y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def password():
    lista = ["Ingrese Contrasena y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def comprador(cadena):
    query = "SELECT nombre_usuario FROM usuarios WHERE email = '%s'" % cadena
    result = run_query(query)
    usuario = json.dumps(result)
    return usuario


def reportes():
    lista = ["Contenido del Archivo Log Usuarios"]
    lineas = (l.rstrip('\n') for l in file("datos.txt", "Ur"))
    for l in lineas:
        lista.append(l)
        cadena = json.dumps(lista)
        return cadena

def maximo():
    query = "SELECT sum(pago_ganador) FROM aciertos"
    result = run_query(query)
    cadena = json.dumps(result)
    valor =[["20000000.0"]]
    print cadena
    if cadena > valor:
        lista = ["No se puede realizar mas chances, Excedio el limite de pago"]
    else:
        lista = ["No hay problemas de limite de pago"]

    enviar = json.dumps(lista)
    return enviar


def validar_usuario(cadena):
    lista =[[cadena]]
    query = "SELECT email FROM usuarios WHERE email = '%s'" % cadena
    result = run_query(query)
    usuario = json.dumps(result)
    validar = json.dumps(lista)

    if(usuario == validar):
        return True
    else:
        return False


def validar_contrasena(comprador,cadena,ip):
    lista =[[comprador,cadena]]
    query = "SELECT email,contrasena FROM usuarios WHERE email = '%s' and contrasena = '%s'" % (comprador,cadena)
    result = run_query(query)
    contrasena = json.dumps(result)
    validar_c = json.dumps(lista)

    if(contrasena == validar_c):
        archivo = open('datos.txt', 'a')
        fecha = time.strftime("%x")
        hora = time.strftime("%X")
        archivo.write("Inicio de Sesion Exitoso, ")
        archivo.write("Usuario: " + comprador + ', ')
        archivo.write("Ip: " + str(ip) + ', ')
        archivo.write("Fecha: " + fecha + ', ')
        archivo.write("Hora: " + hora+ '\n')
        archivo.close()
        return True
    else:
        archivo = open('datos.txt', 'a')
        fecha = time.strftime("%x")
        hora = time.strftime("%X")
        archivo.write("Inicio de Sesion Fallido, ")
        archivo.write("Usuario " + comprador + ', ')
        archivo.write("Ip " + str(ip) + ', ')
        archivo.write("Fecha " + fecha + ', ')
        archivo.write("Hora " + hora + '\n')
        archivo.close()
        return False

def convertir(dia):

    if dia == "Monday":
        dia_loteria = "Lunes"
    if dia == "Tuesday":
        dia_loteria = "Martes"

    if dia == "Wednesday":
        dia_loteria = "Miercoles"

    if dia == "Thursday":
        dia_loteria = "Jueves"

    if dia == "Friday":
        dia_loteria = "Viernes"

    if dia == "Saturday":
        dia_loteria = "Sabado"

    if dia == "Sunday":
        dia_loteria = "Domingo"

    return dia_loteria

def adios():
    cadena = "salir"
    return cadena









