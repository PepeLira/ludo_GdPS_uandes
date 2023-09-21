from .Jugador import Jugador
import random
import time

class GameFlow:
  def __init__(self, num_players=4):
    self.game_board_states = []
    self.run_game_sim(num_players)

  def tirar_dado(self):
    return random.randint(1, 6)

  def mostrar_info(self, jugadores):
    for i in jugadores:
      diccionario = {}
      contador = 0
      while contador < 4:
        diccionario[i.color_jugador + str(contador+1)] = i.lista_fichas[contador].posicion
        contador += 1
      print(diccionario)

  def get_board_state(self, jugadores, dice_number, color_jugador):
    board_state = {"base_tokens": [], # el primer juador tiene 3 tokens en la base
                    "common_path": [],  
                    "glory_paths": [],
                    "winner_tokens": [], # no hay fichas en el espacio ganador
                    "winner": False,
                    "dice": dice_number,
                    "current_player": color_jugador}
    
    fichas_jugadores = []
    for jugador in jugadores:
      fichas = []
      contador = 0
      while contador < 4:
        fichas.append(jugador.lista_fichas[contador].posicion)
        contador += 1
      fichas_jugadores.append(fichas)

      # check for tokens in base
      tokensinbase = fichas.count(0)
      board_state["base_tokens"].append(tokensinbase)

      # check for winner tokens
      winner_tokens = sum(1 for item in fichas if isinstance(item, str) and 'WIN' in item)
      board_state["winner_tokens"].append(winner_tokens)
      fichas = [0 for i in fichas if isinstance(i, str) and 'WIN' in i] + [i for i in fichas if isinstance(i, int)] + [i for i in fichas if isinstance(i, str) and 'WIN' not in i]  

      if winner_tokens == 4:
        board_state["winner"] = True

      # Insolate the glory path
      glory_path = [int(i[1]) for i in fichas if isinstance(i, str)] + [0 for i in fichas if isinstance(i, int)]
      board_state["glory_paths"].append(glory_path)
      fichas = [i for i in fichas if isinstance(i, int)] + [0 for i in fichas if isinstance(i, str)]

      # Insolate the common path
      board_state["common_path"].append(fichas)

    return board_state

          
  def run_game_sim(self, num_players):
    jugadores = []

    colores = ["red", "green", "blue", "yellow"] #Hay que hacer una funcion que ordene quien saca el numero mayor

    for i in range(num_players):
      jugador = Jugador(colores[i])
      jugadores.append(jugador)

    while True:
      for e in jugadores:
        while True:
          jugar_dado = self.tirar_dado()
          e.sacar_ficha(jugar_dado)
          self.game_board_states.append(self.get_board_state(jugadores, jugar_dado, e.color_jugador))
          if jugar_dado == 6 or jugar_dado == 1:
            pass
          else:
            break
        if e.ganador():
          break
      if e.ganador():
        break

if __name__ == "__main__":
  GameFlow()
