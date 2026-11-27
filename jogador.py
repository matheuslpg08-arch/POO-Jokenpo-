import random
from jogada import Jogada

class Jogador:
    def __init__(self):
        self.opcoes_validas = ["pedra", "papel", "tesoura"]
        self.escolha_atual = None

    def fazer_escolha_humana(self, entrada):
        entrada = entrada.lower().strip()
        if entrada in self.opcoes_validas:
            self.escolha_atual = Jogada(entrada)
            return True
        return False

    def fazer_escolha_computador(self):
        escolha_computador = random.choice(self.opcoes_validas)
        self.escolha_atual = Jogada(escolha_computador)
        return self.escolha_atual