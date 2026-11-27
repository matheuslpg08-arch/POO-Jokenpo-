from jogador import Jogador

class PPT:
    def __init__(self):
        self.jogador = Jogador()
        self.computador = Jogador()

    def iniciar(self):
        
        entrada_jogador = input("Escolha (pedra, papel ou tesoura): ")

        if not self.jogador.fazer_escolha_humana(entrada_jogador):
            print("Jogada inválida! Tente novamente.")
            return

        comp_jogada = self.computador.fazer_escolha_computador()
        print(f"Computador escolheu: {comp_jogada.nome}")

        jogada_h = self.jogador.escolha_atual

        if jogada_h.nome == comp_jogada.nome:
            print("Empate!")
        elif jogada_h.vence_de(comp_jogada):
            print("Você venceu!")
        else:
            print("Você perdeu!")