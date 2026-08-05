#Declaração de Classe
class Gafanhoto:
    """
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.
    para criar uma nova pessoa, use a variável = Gafanhoto()
    """
    def __init__(self, nome = "", idade=0): #Método Construtor
        # Atributos de Instância
        self.nome = nome       #n e i são os parâmetros da função que viraram atributos
        self.idade = idade


    #Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1


    def __str__(self):          #dunder method vai escrevar a mensagem
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."


    def __getstate__(self):
        return f" Estado: nome = {self.nome}; idade = {self.idade} "


#Declaração de Objetos
g1 = Gafanhoto("Louren", 32)                #Chamada para o método construtor(__init__)
g1.aniversario()
print(g1.__getstate__())           #G1 com parênteses () é um método

g2 = Gafanhoto("Letícia", 25)
g2.aniversario()
print(g2.__getstate__())

#print(g1.__doc__) #Dunder Attribute, vai trazer a informação quando for adicionado em uma docstings
#print(g1.__dict__)         #vai mostrar o conteúdo dos atribuídos em formato de dicionário (atributo)
#print(g1.__getstate__())  #mesma função do anterior (método) pode ser personalizado
print(g1.__class__)     #vai mostrar qual a classe de objeto que foi solicitado nesse caso g1