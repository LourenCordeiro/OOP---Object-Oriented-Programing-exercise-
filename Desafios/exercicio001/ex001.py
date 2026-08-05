#Declaração de Classe
class Gafanhoto:
    def __init__(self): #Método Construtor
        # Atributos de Instância
        self.nome = ""
        self.idade = 0


    #Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1


    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."


#Declaração de Objetos
g1 = Gafanhoto()                #Chamada para o método construtor(__init__)
g1.nome = "Maria"               #G1 sem parênteses () é um atributo
g1.idade = int(input('Digite uma idade: '))
g1.aniversario()
print(g1.mensagem())            #G1 com parênteses () é um método

g2 = Gafanhoto()
g2.nome = "José"
g2.idade = 45
g2.aniversario()
print(g2.mensagem())