#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *
from configuracion import *
from funciones import *
from extrasFINAL import *

#Funcion principal
def main():
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #pygame.mixer.init()

        #Preparar la ventana
        pygame.display.set_caption("Pasa palabra...")
        screen = pygame.display.set_mode((ANCHO, ALTO))
##        pygame.mixer.music.load("new-york-jazz-loop.wav")#Musica de fondo
        #tiempo total del juego
##        sonido=pygame.mixer.Sound("switch.wav")#Sonido de teclas
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial
        puntos = 0
        candidata = ""
        listaFrases=[]
##        findejuego = pygame.image.load("findejuego.png")
        #lectura del diccionario
        listaPalabrasDiccionario=lectura2("lemario.txt")

        #lectura del archivo. Cada linea es una frase
        listaLectura=lectura("Matrix1999.srt")

        #de cada frase elige la palabra mas larga
        larga=longitud_minima(listaLectura)
        #da comienzo a la musica de fondo
##        pygame.mixer.music.play()
        #elige una al azar
        azar = nueva_palabra(larga)
        long = len(azar)

        ocultar_palabra=salida(nueva_palabra(larga))

        dibujar(screen, candidata, azar, ocultar_palabra, puntos,segundos)

        while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:
            	fps = 3

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    candidata += letra
##                    sonido.play()
                    if e.key == K_BACKSPACE:
                        candidata = candidata[0:len(candidata)-1]
                    if e.key == K_RETURN:
                        puntos += procesar(candidata,azar, listaPalabrasDiccionario)
                        azar=nueva_palabra(larga)
                        ocultar_palabra=salida(azar)
                        candidata = ""

            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            #Dibujar de nuevo todo
            dibujar(screen, candidata, azar, ocultar_palabra, puntos,segundos)



            pygame.display.flip()

        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return

#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()