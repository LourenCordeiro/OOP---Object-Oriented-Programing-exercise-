from abc import ABC, abstractmethod


class BebidaQuente(ABC):


    def __init__(self):
        self.preparar()
 
    @abstractmethod
    def misturar(self):
        pass

    def servir(self):
        pass

    def ferver_agua(self):
        print("1. Fervendo água a 100 graus Celsios.")

    def preparar(self):
        self.ferver_agua()
        self.misturar()
        self.servir()

class Cafe(BebidaQuente):

    def __init__(self):
        super().__init__()

    def misturar(self):
        print("2. Passando água pressurizada pelo pó de café moído.")

    def servir(self):
        print("3. Servindo em xícara pequena")


class Cha(BebidaQuente):

    def __init__(self):
        super().__init__()

    def misturar(self):
        print("2. Mergulhando o sachê de ervas na água.")

    def servir(self):
        print("3. Servindo na cacneca de porcelana com limão.")


class Leite(BebidaQuente):
    
    def __init__(self):
        super().__init__()

    def misturar(self):
        print("2.Pasando vapor pressurizado pelo bico do leite.")

    def servir(self):
        print("3.Servindo na caneca grande, já com café")

