from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel 

class Funcionario(ABC):
    sal_min = 1612
    inss = 7.5

    def __init__(self, nome, sal_bruto):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = 0 

    @abstractmethod
    def calcular_salario(self):
        pass

    def analisar_salario(self):
        analisar = self.salario / self.sal_min
        painel = Panel(
            f"O salário de [blue]{self.nome}[/]({self.__class__.__name__}) é de [green]R${self.salario:.2f}[/]"
            f" e corresponde a [yellow]{analisar:.2f} salários mínimos[/]. ",
            title="Análise de Salário", width=40,
        )    
        print (painel)


class Horista(Funcionario):

    def __init__(self, nome, valor_hora, qtd_horas=220):
        sal_bruto = valor_hora * qtd_horas
        super().__init__(nome, sal_bruto)
        self.valor_hora = valor_hora
        self.qtd_horas = qtd_horas

    def calcular_salario(self):
        desconto = self.sal_bruto * self.inss / 100
        self.salario = self.sal_bruto - desconto

        

class Mensalista(Funcionario):

    def __init__(self, nome, sal_bruto):
        super().__init__(nome, sal_bruto)
        self.sal_bruto = sal_bruto

    def calcular_salario(self):
        desconto = self.sal_bruto * self.inss / 100
        self.salario = self.sal_bruto - desconto

