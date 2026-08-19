class Avaliacao:

    def __init__(self, nome, disciplina, nota=0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota           #Atributo protegido


    #Criando Atributo Validável
    @property
    def nota(self):     #getter
        return self._nota

    @nota.setter 
    def nota(self, valor):      #setter
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print("Nota inválida")


    @nota.deletter   #Usa uma validação para excluir    
    def nota(self):
        pass



