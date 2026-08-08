from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = []

    
    def add_favoritos(self, jogo):
        self.favoritos.append(jogo) 

    def ficha(self):
        texto = "\n".join(f":video_game: {jogo}" for jogo in self.favoritos)
#        texto = ""
#        for jogo in self.favoritos:
#            texto += jogo + "\n"

        conteudo = (
            f"Nome real: {self.nome}\n"
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

