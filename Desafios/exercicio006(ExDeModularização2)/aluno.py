from pessoa import Pessoa

class Aluno(Pessoa):                    #aqui a classe "Pessoa" entre parênteses liga os atributos da classe mãe
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)           #comando para trazer os atributos solicidades da classe mãe
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"{self.nome} acabou de fazer matrícula")