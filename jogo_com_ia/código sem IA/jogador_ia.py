# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        super().__init__(tabuleiro, tipo)
            

    def getJogada(self) -> (int, int):
        #R1- Se você tiver duas marcações em sequência, marque o quadrado restante.
        for l in range(0,3):
            vazio = None
            somal = 0

            for c in range(0,3):
                somal = somal + self.matriz[l][c]
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    vazio = (l,c) #se ha um quadrado vazio guarda a posicao para marcar se necessario
                if somal == 2 and vazio is not None:
                    return vazio
        
        for c in range(0,3):
            vazio = None
            somac = 0

            for l in range(0,3):
                somac = somac + self.matriz[l][c]
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    vazio = (l,c)
                if somac == 2 and vazio is not None:
                    return vazio
        
        somad = 0
        vazio = None
        for d in range(0,3):
            somad = somad + self.matriz[d][d]

            if self.matriz[d][d] == Tabuleiro.DESCONHECIDO:
                vazio = (d,d)
                
            if somad == 2 and vazio is not None:
                return vazio
            
        c = 2
        somadi = 0
        vazio = None
        for l in range(0,3): 
            somadi = somadi + self.matriz[l][c]

            if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                vazio = (l,c)

            if somadi == 2 and vazio is not None:
                return vazio
            
            c = c - 1
        
        #R1.5- Se o seu oponente tiver duas marcações em sequência, marque o quadrado restante.
        for l in range(0,3):
            vazio = None
            somal = 0

            for c in range(0,3):
                somal = somal + self.matriz[l][c]
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    vazio = (l,c)
                if somal == 8 and vazio is not None:
                    return vazio
        
        for c in range(0,3):
            vazio = None
            somac = 0

            for l in range(0,3):
                somac = somac + self.matriz[l][c]
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    vazio = (l,c)
                if somac == 8 and vazio is not None:
                    return vazio
        
        somad = 0
        vazio = None
        for d in range(0,3):
            somad = somad + self.matriz[d][d]

            if self.matriz[d][d] == Tabuleiro.DESCONHECIDO:
                vazio = (d,d)
                
            if somad == 8 and vazio is not None:
                return vazio
            
        c = 2
        somadi = 0
        vazio = None
        for l in range(0,3): 
            somadi = somadi + self.matriz[l][c]

            if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                vazio = (l,c)

            if somadi == 8 and vazio is not None:
                return vazio
            
            c = c - 1

        #R2- Se houver uma jogada que crie duas sequências de duas marcações, use-a.
        for l in range(0,3):
            for c in range(0,3):
                soma = 0
                if self.matriz[l][c] == 0:
                    #verificando a linha
                    for x in range(0,3):
                        soma = soma + self.matriz[x][c]
                    #verificando a coluna
                    for y in range(0,3):
                        soma = soma + self.matriz[l][y]
                    #se for na diagonal:
                    if l == c and soma != 2:
                        for d in range(0,3):
                            soma = soma + self.matriz[d][d]

                if soma == 2:
                    return (l,c)


        #R3- Se o quadrado central estiver livre, marque-o.
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1,1)
        
        #R4- Se seu oponente tiver marcado um dos cantos, marque o canto oposto.
        if self.matriz[0][0] == 4 and self.matriz[2][2] == 0:
            return (2,2)

        if self.matriz[0][2] == 4 and self.matriz[2][0] == 0:
            return (2,0)
        
        if self.matriz[2][0] == 4 and self.matriz[0][2] == 0:
            return (0,2)
        
        if self.matriz[2][2] == 4 and self.matriz[0][0] == 0:
            return (0,0)

        #R5- Se houver um canto vazio, marque-o.
        if self.matriz[0][0] == 0:
            return (0,0)
        
        if self.matriz[0][2] == 0:
            return (0,2)
        
        if self.matriz[2][0] == 0:
            return (2,0)
        
        if self.matriz[2][2] == 0:
            return (2,2)

        #R6- Marque arbitrariamente um quadrado vazio.
        lista = []
        for l in range(0,3):
            for c in range(0,3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    lista.append((l, c))
                    
        if(len(lista) > 0):
            p = randint(0, len(lista)-1)
            return lista[p]
        else:
           return None