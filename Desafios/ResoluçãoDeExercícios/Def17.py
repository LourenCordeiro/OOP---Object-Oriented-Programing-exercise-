from rich import print
from rich.table import Table


class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco


    def etiqueta(self):
        tabela = Table(title='Produto')
        tabela.add_column('nome')
        tabela.add_column('preco')
        tabela.add_row(self.nome, f"R$ {self.preco:,.2f}")
        print(tabela)




p1 = Produto('iPhone 17 Pro Max', 25_000.85)
p2 = Produto('Notebook Gamer', 8_000)

p1.etiqueta()
p2.etiqueta()
