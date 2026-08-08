from rich import print

class Caneta:
    def __init__(self, cor):
        self.cor = cor 
        self.destampada = False

    def destampar(self):
        self.destampada = True

    def tampar(self):
        self.destampada = False

    def escrever(self, frase):
        if not self.destampada:
            raise RuntimeError("A caneta está tampada - destampe antes de escrever.")

        if self.cor == 'azul':
         return f"[blue]{frase}[/]"
        elif self.cor == 'vermelha':
            return f"[red]{frase}[/]"
        elif self.cor == 'verde':
            return f"[green]{frase}[/]"
        else:
            return frase


c1 = Caneta('azul')
c2 = Caneta('vermelha')
c3 = Caneta('verde')

c1.destampar()
c2.destampar()
c3.destampar()

print(c1.escrever("Olá tudo bem?"))
print(c2.escrever("Como foi seu dia?"))
print(c3.escrever("Como foi o trabalho?"))


#resolução realizada pelo proessor trouxe o uso de "macth/escolha/case" sendo uma alternativa para o uso de laço que eu fiz

#from rich import print

#class Caneta:
#    def __init__(self, cor='azul'):
#        escolha = ""
#        match cor.lower().strip():
#            case "azul":
#                escolha = "[blue]"
#            case "vermelho" | "vermelha":
#                escolha = "[red]"
#            case "verde":
#                escolha = "[green]"
#            case _:                              #esse comando faz com que quando n seja escolhido nenhuma cor definida ela seja branca 
#                escolha = "[white]"         
        
#        self.cor = escolha
#        self.tampada = True

#    def escrever(self, msgn):
#        if self.tampada:
#            print(f":prohibited: A {self.cor}caneta[/] está tampada! ")
#        else:
#            print(f"{self.cor}{msgn}[/]", end='')

#    def quebrar_linha(self, qtd=1):
#        print("\n" * qtd, end="")

#    def tampar(self):
#        self.tampada = True

#    def destampar (self):
#        self.tampada = False


#c1 = Caneta('azul')
#c2 = Caneta('vermelha')
#c3 = Caneta('verde')

#c1.destampar()
#c2.destampar()
#c3.destampar()

#c1.escrever('Olá, Mundo!')
#c1.quebrar_linha(2)
#c2.escrever('Exercício funcional para aprender o uso efetivo de funções e objetos.')
#c2.quebrar_linha(2)
#c3.escrever('Informação de "Case" é nova e muito interessante.')







