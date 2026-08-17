from abc import ABC, abstractmethod
import random
from rich import print
from rich.panel import Panel 


class Personagem(ABC):

    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida 
        self. golpes = []

    def atacar(self, alvo, forca=100):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes [random.randrange(0, len(self.golpes))]
            print(f"[green]{self.nome}[/]({self.vida}) atacou [red]{alvo.nome}[/]({alvo.vida}) com um [blue]{golpe}[/] de força máxima {forca} ")
            alvo.receber_dano(forca)
        

    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida = self.vida - fator
        if self.vida < 0:
            self.vida = 0
            print(f"{self.nome} morreu!")
        print(f"[red]{self.nome}[/] recebeu {fator} de danos.")

    @abstractmethod
    def curar(self):
        pass

    def status_jogo(self, alvo):
        
        painel = Panel(
            f"O jogador [green]{self.nome}[/] finalizou a rodadd com [blue]{self.vida}[/] pontos de vida e o jogador [green]{alvo.nome}[/] finalizou com [blue]{alvo.vida}[/] pontos de vida.",
            title='Status dos Jogadores', width=40,
        )
        print(painel)


class Guerreiro(Personagem):

    def __init__(self, nome, vida):
            super().__init__(nome, vida)
            self.golpes = ["Golpe de Machado", "Golpe com Escudo", "Pulo Giratório"]

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f"[green]{self.nome}[/] enrolou uma atadura nos ferimentos e [green]recuperou {fator} pontos[/] de vida.")
        


class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Magia de ataque", "Escudo de Defesa", "Esquiva Furtiva"]

    def curar(self):
        fator = random.randint(0, 200)
        self.vida += fator
        print(f"[green]{self.nome}[/] usou magia de cura e [green]recuperou {fator} pontos[/] de vida.\n")
        


