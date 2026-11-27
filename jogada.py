class Jogada:
    def __init__(self, nome):
        self.nome = nome

    def vence_de(self, outra_jogada):
        regras = {
            "pedra": "tesoura",
            "tesoura": "papel",
            "papel": "pedra"
        }
        return regras[self.nome] == outra_jogada.nome