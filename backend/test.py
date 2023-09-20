import random

def comenzar_juego(jugadores):
    if len(jugadores) < 2 or len(jugadores) > 4:
        return "La lista de jugadores debe contener entre 2 y 4 jugadores."

    puntajes = {jugador: 0 for jugador in jugadores}
    for jugador in jugadores:
        puntajes[jugador] = random.randint(1, 6)

    print(puntajes)
    puntaje_maximo = max(puntajes.values())

    jugadores_empate = [jugador for jugador, puntaje in puntajes.items() if puntaje == puntaje_maximo]

    if len(jugadores_empate) > 1:
        return comenzar_juego(jugadores_empate)

    jugador_comienza = jugadores_empate[0]

    return jugador_comienza


jugadores = ["rojo", "azul", "amarillo", "verde"]
resultado = comenzar_juego(jugadores)
print(resultado)

class Ficha:
    def __init__(self, color, indice):
        self.color = color
        self.indice = indice

# Supongamos que tienes una lista de objetos Ficha
fichas = [Ficha("rojo", 3), Ficha("azul", 1), Ficha("verde", 1), Ficha("amarillo", 2)]

ficha_con_menor_indice = min(fichas, key=lambda x: x.indice)

print("La ficha con el menor índice es de color:", ficha_con_menor_indice.color)
print("El índice más pequeño es:", ficha_con_menor_indice.indice)




