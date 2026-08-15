#from abc import ABC, abstractmethod


#class Transporte(ABC):
#
#    def __init__(self, distancia, fator):
#        self.distancia = distancia
#        self.fator = fator#

#    @abstractmethod
#    def calc_frete(self):
#        pass


#class Moto(Transporte):
#    def __init__(self, distancia, fator=0.50):
#        super().__init__(distancia, fator)

#    def calc_frete(self):
#        return self.fator * self.distancia


#class Caminhao(Transporte):
#    RAIO_MINIMO = 50

#    def __init__(self, distancia,  fator = 1.20):
#        super().__init__(distancia, fator)

#    def calc_frete(self):
#        if self.distancia <= self.RAIO_MINIMO:
#            raise ValueError (f"Raio mínimo de {self.RAIO_MINIMO}Km para caminhão")
#        return self.fator * self.distancia


#class Drone(Transporte):
#    RAIO_MAXIMO = 10
 
#    def __init__(self, distancia,  fator = 9.50):
#        super().__init__(distancia, fator)

#    def calc_frete(self):
#        if self.distancia >= self.RAIO_MAXIMO:
#            raise ValueError (f"Raio máximo de {self.RAIO_MAXIMO}Km para drone")
#        return self.fator * self.distancia


#a resolução do exercício pelo professor, 
from abc import ABC, abstractmethod


class Transporte(ABC):
    
    def __init__(self, distancia):      #distância é um atributo que será passado um valor por isso precisa estar no método construtor
        self.distancia = distancia      #enquanto frete será calculado no código
        self.frete = 0

    @abstractmethod
    def calcular_frete(self):
        pass


class Moto(Transporte):
    fator = 0.50                #Atributo da classe
    
    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        self.frete = self.distancia * Moto.fator    #Atributos de classe precisam vir seguidos da classe
        return f"R$ {self.frete:.2f}"

class Caminhao(Transporte):
    fator = 1.20

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia < 50:
            self.frete = 0
            return "Raio mínimo de 50Km"
        else:
            self.frete = self.distancia * Caminhao.fator
            return f"R$ {self.frete:.2f}"


class Drone(Transporte):
    fator = 9.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia > 10:
            self.frete = 0
            return "Raio máximo de 10Km"
        else:
            self.frete = self.distancia * Drone.fator
            return f"R$ {self.frete:.2f}"
