from jogador import Jogador

class PPT:
    def __init__(self):
        self.jogador = Jogador()
        self.computador = Jogador()
        self.pontos_jogador = 0
        self.pontos_computador = 0

    def iniciar(self):
        print("=== BEM-VINDO AO JOKENPÔ ===")
        
        while True:
            entrada_jogador = input("\nEscolha (pedra, papel ou tesoura): ")

            if not self.jogador.fazer_escolha_humana(entrada_jogador):
                print("Jogada inválida! Tente novamente.")
                continue

            comp_jogada = self.computador.fazer_escolha_computador()
            print(f"Computador escolheu: {comp_jogada.nome}")

            jogada_h = self.jogador.escolha_atual

            if jogada_h.nome == comp_jogada.nome:
                print("Empate!")
            elif jogada_h.vence_de(comp_jogada):
                print("Você venceu esta rodada!")
                self.pontos_jogador += 1
            else:
                print("Você perdeu esta rodada!")
                self.pontos_computador += 1

            print(f"Placar atual -> Você: {self.pontos_jogador} | Computador: {self.pontos_computador}")

            continuar = input("\nDeseja jogar outra rodada? (s/n): ").lower().strip()
            if continuar != 's':
                print("\n=== FIM DE JOGO ===")
                print(f"Placar final -> Você: {self.pontos_jogador} | Computador: {self.pontos_computador}")
                print("Obrigado por jogar!")
                break