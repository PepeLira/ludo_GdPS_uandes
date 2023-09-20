from Ficha import Ficha
import time

class Jugador:
    def __init__(self, color_jugador):
        self.color_jugador = color_jugador

        if color_jugador == 'red':
            self.casillas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'RWIN']
        elif color_jugador == 'blue':
            self.casillas = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'BWIN']
        elif color_jugador == 'yellow':
            self.casillas = [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'YWIN']
        elif color_jugador == 'green':
            self.casillas = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'GWIN']

        self.lista_fichas = []

        contador = 0
        while contador < 4:
            ficha = Ficha(color_jugador)
            self.lista_fichas.append(ficha)
            contador += 1

    def sacar_ficha(self, numero_dado):
        var = 0
        if numero_dado == 6 or numero_dado == 1:
            for i in self.lista_fichas: 
                if i.posicion == 0:
                    i.posicion = self.casillas[0]
                    var = 1
                    break
        if var == 0:
            self.avanzar_ficha(numero_dado)

    def avanzar_ficha(self, numero_dado):
        fichas_iniciadas = []
        for i in self.lista_fichas:
            if i.posicion == 0:
                pass
            else:
                fichas_iniciadas.append(i)

        if len(fichas_iniciadas) != 0:
            ficha_menor = min(fichas_iniciadas, key=lambda x: x.indice)
            nueva_posicion = ficha_menor.indice + numero_dado

            if nueva_posicion >= len(self.casillas):
                nueva_posicion = len(self.casillas) - 1

            ficha_menor.indice = nueva_posicion
            ficha_menor.posicion = self.casillas[nueva_posicion]
            self.comer_ficha(ficha_menor.posicion)
        else:
            pass

    def ganador(self):
        for i in self.lista_fichas:
            if i.posicion != self.casillas[-1]:
                return False
        return True
    
    def comer_ficha(self, nueva_posicion):
        for i in self.lista_fichas:
            if i.color != self.color_jugador:
                print(self.color_jugador, "COMIO A FICHA", i.color)
                if i.posicion == nueva_posicion:
                    i.posicion = 0
                    i.indice = 0
                    time.sleep(3)



