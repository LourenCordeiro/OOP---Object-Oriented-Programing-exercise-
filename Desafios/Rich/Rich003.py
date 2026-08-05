from rich import print
from rich.table import Table

tabela = Table(title='Tabela de Preços')

tabela.add_column('Nome', justify='center', style='cyan')
tabela.add_column('Preço', justify='right', style='green')
tabela.add_row('Feijão', 'R$ 10,00')
tabela.add_row('Arroz', 'R$ 15,00')
tabela.add_row('Carne', 'R$ 20,00')
tabela.add_row('Frutas', 'R$ 25,00')
tabela.add_row('Legumes', 'R$ 30,00')

print(tabela)
