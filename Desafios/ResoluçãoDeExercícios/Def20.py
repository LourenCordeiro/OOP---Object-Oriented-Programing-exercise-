from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = []         #é possível criar lista, tuplas e dicionários como atributo para armazenar informações

    
    def add_favoritos(self, jogo):
        self.favoritos.append(jogo) 
        

    def ficha(self):
        texto = "\n".join(f":video_game: {jogo}" for jogo in self.favoritos)
#        texto = ""
#        for jogo in self.favoritos:
#            texto += jogo + "\n"

        conteudo = (
            f"Nome real: [black on blue] {self.nome} [/]\n"
            f"Jogos Favoritos:\n"
            f"[blue]{texto}[/]"
        )

        caixa = Panel(conteudo, title=f"Jogador:<{self.nick}>", width=40)
        print(caixa)


j1 = Gamer("Fabrício Silva", "detonador2025")
j1.add_favoritos("Fortnite")
j1.add_favoritos("God of War")
j1.add_favoritos("Mario Bros")
j1.add_favoritos("Sonic")
j1.ficha()


j2 = Gamer("Olívia Souza", "peach_raivosa")
j2.add_favoritos("Mario Bros")
j2.add_favoritos("Call of Duty")
j2.ficha()

#O seguinte código foi o realizado pelo professor na correção do exercício, atenção ao uso de do "for" na minha opinião foi mais eficiente

#from rich import print
#from rich.panel import Panel
#from rich import inspect


#class Gamer:
#    def __init__(self, nome, nick):
#        self.nome = nome
#        self.nick = nick 
#        self.favoritos = []

#    def add_favoritos(self, game):
#        self.favoritos.append(game)
#        self.favoritos = sorted(self.favoritos, key=str.lower)          #esse comando vai colocar em ordem alfabética tudo que for adicionado como game

#    def ficha(self):
#        conteudo = f"Nome real: [black on blue] {self.nome} [/]"
#        conteudo += f"\nJogos favoritos:"
#        for num, game in enumerate (self.favoritos):
#            conteudo += f"\n:video_game: [blue]{game}[/]"
#        painel = Panel(conteudo, title=f"Jogador <{self.nick}>", width=40)
#        print(painel)


#j1 = Gamer("Fabrício Silva", "detonador2025")
#j1.add_favoritos("Fortnite")
#j1.add_favoritos("God of War")
#j1.add_favoritos("Mario Bros")
#j1.add_favoritos("Sonic")
#j1.ficha()
#inspect(j1)            #comando inspect utilizado para verificar aos parâmetros

#j2 = Gamer("Olívia Souza", "peach_raivosa")
#j2.add_favoritos("Mario Bros")
#j2.add_favoritos("Call of Duty")
#j2.ficha()
#inspect(j2)

