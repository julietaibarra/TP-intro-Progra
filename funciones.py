 #!/usr/bin/env python
#-*-coding:utf-8 -*-
# -*- coding:Windows 1252 -*-
from string import*
import string
import random
def acentos(txt):
    """ recibe txt origina de matrix, elimina los acentos.
    salida : txt sin acentos.
    restriccion: ninguna."""
    vocales_acento = "áéíóúÁÉÍÓÚñÑ"
    vocales = "aeiouAEIOUnN" #aeiouAEIOU
    tx  = txt.maketrans(vocales_acento,vocales)
    return txt.translate(tx)
def txt_limpio(txt):
    cadena_limpia = ""
    abc ="abcdefghijklmnopqrstuvwxyz' '\n"
    for elemento in txt:
        for letra in elemento:
            letra = letra.lower()
            if letra in abc:
                cadena_limpia += letra
    return cadena_limpia

def lectura(txt):
    #lectura del archivo Matrix1999
    archivo = open(txt,"r")
    cadena = ""
    for linea in archivo.readlines():
    		cadena += acentos(linea)
    var = txt_limpio(cadena).split()
    archivo.close()
    return var
listaLectura=lectura("Matrix1999.srt")
def longitud_minima(lista):
    #Elige palabras con una longitud minima de 5 caracteres
    cont=1
    listamax=[]
    cantidad_caracter=""
    for elemento in lista:
        cantidad_caracter+=elemento
        cont=len(elemento)
        if cont>5:
            listamax.append(elemento)
    return listamax

def nueva_palabra(lista):
    """ recibe una lista.
    salida: un elemento al azar de la lista.
    restriccion: ninguna."""
    elemento_azar = random.choice(lista)
    return elemento_azar

def salida(txt):
    """ recibe una palabra.
    salida: palabra oculta por *.
    resticcion: ninguna"""
    larga = len(txt)
    azar = 0
    oculta = ""
    for i in range (2):

        azar = random.randint(0,larga-1)
        txt = txt.replace(txt[azar],"*")
    return txt
larga=longitud_minima(listaLectura)
azar= nueva_palabra(larga)
ocultar_palabra= salida(azar)
"""lectura del archivo lemario"""
def lectura2(txt):
    archivo2 = open(txt,"r")
    leer = archivo2.readlines()
    lista=[]
    for letra in leer:
        letra=letra[0:-1]
        lista.append(letra)
    archivo2.close()
    return lista
listaPalabrasDiccionario=lectura2("lemario.txt")
def valida(candidata,ocultar_palabra, azar):
    #verifica que la palabra es valida
    if ocultar_palabra==azar:
        if azar==candidata:
            return True
    return False

def puntos(candidata,azar, listaPalabrasDiccionario):
    #Calcula los puntos
    long = len(azar)
    puntos=0
    if azar  == candidata:
        puntos += long * 5
        ocultar_palabra
    elif candidata in listaPalabrasDiccionario:
        puntos += long
        ocultar_palabra
    else:
        puntos = puntos - long
        ocultar_palabra
    return puntos

def procesar(candidata,azar,listaPalabrasDiccionario):
    #Devuelve el puntaje obtenido
        if valida(candidata,ocultar_palabra, azar):
            puntosObtenidos=puntos(candidata,azar, listaPalabrasDiccionario)
        else:
            puntosObtenidos=puntos(candidata,azar, listaPalabrasDiccionario)
        return puntosObtenidos