class Caixinha:
    def __init__(self, valor, eh_pergunta=True):
        self.valor = valor
        self.eh_pergunta = eh_pergunta
        self.sim = None
        self.nao = None

    def eh_folha(self):
        return not self.eh_pergunta


class JogoAdivinhaAnimal:
    def __init__(self):
        self.raiz = Caixinha("cachorro", eh_pergunta=False)
        self.rodando = True

    def _limpar_entrada(self, texto):
        return texto.strip().lower()

    def _jogar_recursivo(self, caixinha_atual):
        if caixinha_atual.eh_folha():
            resposta_final = input(f"Seu animal é um(a) {caixinha_atual.valor}? (sim/nao) ")
            if self._limpar_entrada(resposta_final) == "sim":
                print("Eba! Acertei!")
            else:
                print("Ah, que pena! Eu errei.")
                novo_animal = input("Qual era o seu animal? ")
                nova_pergunta = input(f"Uma pergunta que diferencia um(a) {novo_animal} de um(a) {caixinha_atual.valor} (responda 'sim' para {novo_animal}, 'nao' para {caixinha_atual.valor}): ")

                antigo_animal_caixinha = Caixinha(caixinha_atual.valor, eh_pergunta=False)

                caixinha_atual.valor = nova_pergunta
                caixinha_atual.eh_pergunta = True
                caixinha_atual.sim = Caixinha(novo_animal, eh_pergunta=False)
                caixinha_atual.nao = antigo_animal_caixinha

            print("\nVamos jogar de novo?")
            self.iniciar_jogo()
            return
        else:
            resposta_pergunta = input(f"{caixinha_atual.valor} (sim/nao) ")
            if self._limpar_entrada(resposta_pergunta) == "sim":
                if caixinha_atual.sim is None:
                    print("Erro: caminho 'sim' não definido. Reiniciando o jogo.")
                    self.iniciar_jogo()
                    return
                self._jogar_recursivo(caixinha_atual.sim)
            else:
                if caixinha_atual.nao is None:
                    print("Erro: caminho 'não' não definido. Reiniciando o jogo.")
                    self.iniciar_jogo()
                    return
                self._jogar_recursivo(caixinha_atual.nao)

    def mostrar_menu(self):
        print("\n--- Jogo Adivinhe o Animal ---")
        print("1. Jogar!")
        print("2. Sair")
        print("----------------------------")

    def iniciar_jogo(self):
        if not self.rodando:
            print("Obrigado por jogar! Até a próxima.")
            return

        self.mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print("\nPense em um animal... vou tentar adivinhar!")
            self._jogar_recursivo(self.raiz)
        elif escolha == '2':
            self.rodando = False
            self.iniciar_jogo()
        else:
            print("Opção inválida. Por favor, digite 1 ou 2.")
            self.iniciar_jogo()


jogo = JogoAdivinhaAnimal()
jogo.iniciar_jogo()
