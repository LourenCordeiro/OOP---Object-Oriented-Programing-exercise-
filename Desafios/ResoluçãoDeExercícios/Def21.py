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







