class Ficha:
    def __init__(self, color):
        self.color = color
        self.posicion = 0
        self.indice = 0

    def nueva_posicion(self, avance):
        self.posicion = avance
        
        