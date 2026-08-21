class Termostato:

    def __init__(self):
        self.temperatura = 24
        
    @property
    def temperatura(self):
        return self.__temperatura

 #   @temperatura.setter
 #   def temperatura(self, valor):
 #       if not 16 <= valor <= 30:
 #           raise ValueError("Temperatura deve estar entre 16 e 30 graus.")
 #       if not float(valor * 2).is_integer():
 #           raise ValueError("Temperatura deve variar de 0.5 em 0.5 graus.")
 #       self.__temperatura = valor
    @temperatura.setter
    def temperatura(self, valor):
        if valor % 0.5 != 0:
            raise ValueError(f"Temperatura de {valor}{chr(176)}C é inválida")
        if valor < 16:
            self.__temperatura = 16
        elif valor > 30:
            self.__temperatura = 30
        else:
            self.__temperatura = valor

    @property
    def ftemperatura(self):
        return f"{self.__temperatura}{chr(176)}C"