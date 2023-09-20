from Jugador import Jugador
import random
import time

def tirar_dado():
    return random.randint(1, 6)

def mostrar_info(jugadores):
    for i in jugadores:
        diccionario = {}
        contador = 0
        while contador < 4:
            diccionario[i.color_jugador + str(contador+1)] = i.lista_fichas[contador].posicion
            contador += 1
        print(diccionario)
        

colores = ["red", "blue"] #Hay que hacer una funcion que ordene quien saca el numero mayor
jugadores = []

for i in colores:
    jugador = Jugador(i)
    jugadores.append(jugador)

while True:
    for e in jugadores:
        jugar_dado = tirar_dado()
        print(jugar_dado)
        e.sacar_ficha(jugar_dado)
        mostrar_info(jugadores)

    print("siguiente turno") 
    time.sleep(3)


