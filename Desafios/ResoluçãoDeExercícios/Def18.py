from rich import print
from rich.panel import Panel

consumo_por_pessoa = 0.4
preco_por_kg = 82.40

class Churrasco:
    def __init__(self, titulo, quantidade):
        """
        Foi considerado nesse cáculo o padrão solicitado no enunciado do exercício:
        consumo padrão: 400g por pessoa
        Preço: R$ 82,40/Kg
        Dados para realizadção dos cálculos.
        """
        self.titulo = titulo
        self.quantidade = quantidade
        

    def total_kg(self):
        return self.quantidade * consumo_por_pessoa
         
    def custo_total(self):
        return self.total_kg() * preco_por_kg

    def preco_individual(self):
        return self.custo_total()/self.quantidade


    def analisar(self):
        conteudo = (
            f"Analisando [green]{self.titulo}[/] com [blue]{self.quantidade} convidados[/]\n"
            'Cada participante comerá 0.4Kg e cada Kg custa R$ 82,40\n'
            f'Recomendo [blue]comprar {self.total_kg():.3f}Kg[/] de carne\n'
            f'O custo total será de [green]R${self.custo_total():,.2f}[/]\n'
            f'Cada pessoa pagará [yellow]R${self.preco_individual():.2f}[/] para participar\n'
        )
        caixa = Panel(conteudo, title=self.titulo, width=80)
        print(caixa)


c1 = Churrasco("Churras dos amigos", 15)
c1.analisar()

c2 = Churrasco("Festa de Fim de Ano", 80)
c2.analisar()
