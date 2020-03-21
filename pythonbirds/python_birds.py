# -*- coding: utf-8 -*-
from pythonbirds.atores import PassaroVermelho, PassaroAmarelo, Porco, Obstaculo
from pythonbirds.fase import Fase
from pythonbirds import placa_grafica

fase_exemplo = Fase()
passaros = [PassaroVermelho(3, 3), PassaroAmarelo(3, 3), PassaroAmarelo(3, 3)]
porcos = [Porco(78, 1), Porco(70, 1)]
obstaculos = [Obstaculo(31, 10)]

fase_exemplo.adicionar_passaro(*passaros)
fase_exemplo.adicionar_porco(*porcos)
fase_exemplo.adicionar_obstaculo(*obstaculos)

# Solução para ganhar
# fase_exemplo.lancar(45, 1)
# fase_exemplo.lancar(63, 3)
# fase_exemplo.lancar(23, 4)

if __name__ == '__main__':
    placa_grafica.animar(fase_exemplo)
