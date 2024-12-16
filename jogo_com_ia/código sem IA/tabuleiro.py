# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [ [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO], 
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]]
       
        
    def tem_campeao(self):
        for l in range (0, 3):
            somal = 0
            for c in range (0, 3):
                somal = somal + self.matriz[l][c]

            if somal == 3:
                return Tabuleiro.JOGADOR_0
            elif somal == 12:
                return Tabuleiro.JOGADOR_X

        for c in range (0, 3):
            somac = 0
            for l in range (0, 3):
                somac = somac + self.matriz[l][c]

            if somac == 3:
                return Tabuleiro.JOGADOR_0
            elif somac == 12:
                return Tabuleiro.JOGADOR_X
        
        somad = 0
        for d in range (0, 3):
            somad = somad + self.matriz[d][d]
        
        if somad == 3:
                return Tabuleiro.JOGADOR_0
        elif somad == 12:
                return Tabuleiro.JOGADOR_X

        somad = 0
        somad = self.matriz[0][2] + self.matriz[1][1] + self.matriz[2][0]
        if somad == 3:
                return Tabuleiro.JOGADOR_0
        elif somad == 12:
                return Tabuleiro.JOGADOR_X
        

        return Tabuleiro.DESCONHECIDO