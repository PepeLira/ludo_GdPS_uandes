import array
from token import Token
from dice import Dice 
from player import Player 


class Board():
    def __init__(self) -> None:
        self.board = array.array('u', [Token("W")] * 52)
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
    
    
    def move(self,actual, plus, color):
        position = actual + plus

        if actual + plus > 52:
            position = actual + plus - 52
        
        if color == "R" and position >= 52:
            pass
        if color == "Y" and position >= 52:
            pass
        if color == "B" and position >= 52:
            pass
        if color == "G" and position >= 52:
            pass

        if self.board[position].color != "W":
            for player in self.players:
                if player.color == self.board[position]:
                    player.token_home += self.board[position].number
            
            self.borad[position].color = self.borad[actual].color 
            self.borad[position].number = self.borad[actual].number
            self.borad[actual].color = "W"
            self.borad[actual].number = 0

        else:
            self.borad[position].color = self.borad[actual].color 
            self.borad[position].number = self.borad[actual].number
            self.borad[actual].color = "W"
            self.borad[actual].number = 0


    def out(self,player):
        if player.token_home >= 1:
            player.token_home -= 1
            player.token_in_game += 1
        else:
            return player 
        if player.color == "R":
            self.move(0,0,"R")
        if player.color == "Y":
            self.move(12,0,"Y")
        if player.color == "B":
            self.move(25,0,"B")
        if player.color == "G":
            self.move(35,0,"G")
        return player


    

        
