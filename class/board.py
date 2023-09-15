import array
from token import Token
from dice import Dice 
from player import Player 


class Board():
    def __init__(self) -> None:
        self.board_1 = array.array('u', [Token()] * 52)
        self.board_1[0].color = "R"
        self.board_1[13].color = "Y"
        self.board_1[26].color = "B"
        self.board_1[39].color = "G"
        self.borad_R = array.array('u', [Token("R")] * 6)
        self.borad_Y = array.array('u', [Token("Y")] * 6)
        self.borad_B = array.array('u', [Token("B")] * 6)
        self.borad_G = array.array('u', [Token("G")] * 6)
        self.players = []
        self.dice = Dice()

    def add_player(self,number):
        colors = ["R","Y","B","G"]
        for n in range(number):
            self.players.append(Player(colors[n]))

    def win_game(self):
        for player in self.players:
            if player.token_win>= 4:
                return True
        return False
    
    

        
