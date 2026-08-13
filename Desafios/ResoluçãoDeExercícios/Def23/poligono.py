import math
from abc import ABC, abstractmethod         #ABC é a classe base que você herda para tornar sua classe abstrata
                                            #abstractmethod, um decorador que marca métodos como obrigatórios para as classes filhas

class Poligono(ABC):            #Herdar de ABC é o que a torna abstrata: uma classe que serve de "molde" e não pode ser instanciada diretamente. Se você tentar Poligono(), o Python levanta um erro.
                                # Ela só existe para ser herdada.

    def __init__(self, lados):      #método construtor
        self.qtd_lados = lados

    @abstractmethod             #método abstrato: ele declara que toda classe filha é obrigada a ter esse método, mas não fornece implementação aqui.
    def perimetro(self) -> float:       #método abstrato: ele declara que toda classe filha é obrigada a ter esse método, mas não fornece implementação aqui.
        pass                            #O pass significa basicamente "não faça nada"

    @abstractmethod
    def area(self) -> float:
        pass


class Quadrado(Poligono):           #Quadrado recebe a herança de poligono, obrigatoriamente terá que ter os métodos abstratos


    def __init__(self, lado = 1):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        return self.lado * 4


    def area(self):
        return self.lado ** 2


class Circulo(Poligono):

    def __init__(self, raio = 1 ):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        return 2 * math.pi * self.raio

    def area(self):
        return math.pi * self.raio ** 2
        
