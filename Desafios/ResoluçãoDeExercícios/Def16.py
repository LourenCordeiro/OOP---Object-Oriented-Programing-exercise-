from rich import print
from rich import inspect


class Funcionario:
    #atributos de classe
    empresa = 'Curso em Vídeo'


    def __init__(self, nome, setor, cargo):
        #atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f':handshake: Olá, eu sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}.'


#é possível mudar o atributo da classe e com isso mudar em todos os objetos
Funcionario.empresa = 'Hostnet'


c1 = Funcionario('Maria', 'Administração', 'Diretora')
print(c1.apresentacao())

c2 = Funcionario('Pedro', 'TI', 'Programador')
print(c2.apresentacao())


#inspect(c2)
#vai mostrar as informações solicitadas 