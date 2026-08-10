from abc import ABC, abstractmethod         # Abstract Base Classe
#o comando está inicinado a biblioteca ABC e então chamando o método abstrato

class Pessoa(ABC):
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod             #no momento que crio o abstract method é obrigatório criar o método se não o programa não roda
    def estudar(self):
        pass


class Aluno(Pessoa):                    #aqui a classe "Pessoa" entre parênteses liga os atributos da classe mãe
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)           #comando para trazer os atributos solicidades da classe mãe
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"{self.nome} acabou de fazer matrícula")

    def estudar(self):
        print(f"{self.nome} está estudando {self.curso} na turma {self.turma}")


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"Prof. {self.nome} começou a dar aula")

    def estudar(self):
        print(f"{self.nome} é especialista em {self.especialidade} no {self.nivel}")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"{self.nome} acabou de bater ponto.")
        
    def estudar(self):
        print(f"{self.nome} se especializada para a área {self.setor}")
        