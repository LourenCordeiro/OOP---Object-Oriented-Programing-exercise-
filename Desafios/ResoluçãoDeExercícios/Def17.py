from rich import print
from rich.panel import Panel
from rich.rule import Rule
from rich.console import Group
from rich.text import Text


class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        conteudo = Group(
            Text (self.nome, justify='center'), 
            Rule (characters="-", style="white"),
            Text(f"R${self.preco:,.2f}", justify='center'),
        )
        caixa = Panel(conteudo, title='Produto', style='white', width=40)
        print(caixa)


p1 = Produto('iPhone 17 Pro Max', 25_000.85)
p2 = Produto('Notebook Gamer', 8_000)

p1.etiqueta()
p2.etiqueta()
