import tkinter as tk
import numpy as np
from .ludo_board import LudoBoard

class LudoGame:
    def __init__(self, root):
        self.root = root
        self.board = LudoBoard(self.root)
        self.current_player = None
        self.board_state = {"base_tokens": [4,4,4,4], # [p1 tokens, p2 tokens, p3 tokens, p4 tokens]
                            "common_path": [np.zeros(4) for _ in range(4)], # lista de Nx4 con los indices de cada token (N numero de jugadores) 0 es la base
                            "glory_paths": [np.zeros(4) for _ in range(4)], # lista de Nx4 con los indices de cada token en el paso a la gloria
                            "winner_tokens": [0,0,0,0], # [p1 tokens, p2 tokens, p3 tokens, p4 tokens]
                            "winner": None}

    def start_game(self):
        # Start the game, set up initial conditions, and determine the first player
        self.set_order()
        pass

    def ask_players_number(self):
        self.board.set_board_state(self.board.states[0])
        pass

    def set_order(self):
        self.board.set_board_state(self.board.states[1])
        pass

    def roll_dice(self):
        self.board.set_board_state(self.board.states[2])
        pass

    def move_token(self, player_n, board_state):
        # Move a token for the current player based on the dice roll
        pass

    def is_game_over(self):
        # Check if the game is over (e.g., a player has won)
        pass

    def handle_turn(self):
        # Manage the logic for a player's turn
        pass

    def update_board_state(self, board_state):
        # board_state = {"base_tokens": [1,4,4,4], # el primer juador tiene 3 tokens en la base
        #                     "common_path": [[20,20,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]],  
        #                     "glory_paths": [[0,2,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]],
        #                     "winner_tokens": [0,0,0,0], # no hay fichas en el espacio ganador
        #                     "winner": False}
        self.board_state = board_state
        self.board.set_board_state(board_state)

        


    # def check_collision(self, player, token, steps):
    #     # Check if a token move results in a collision with another token
    #     pass

    # def is_valid_move(self, player, token, steps):
    #     # Check if a move is valid based on game rules
    #     pass