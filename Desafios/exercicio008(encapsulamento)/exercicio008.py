class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, ID, nome, saldo =0):
        self.ID = ID            #público (+)
        self._titular = nome       #protected (#)
        self.__saldo = saldo        #private (-)
        print(f"Conta {self.ID} criada com sucesso. Saldo atual de R${self.__saldo:.2f}")


    def __str__(self):
    #    return f"A conta {self.ID} de {self.titular} tem R${self.saldo:.2f} de saldo."
        return f"Estado atual da conta: {self.__dict__}"

    def depositar (self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Depósito de R${valor:.2f} autorizado na conta {self.ID} ")


    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print(f"Saque NEGADO de R$ {valor:,.2f} na conta {self.ID}: SALDO INSUFICIENTE")
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} autorizado na conta {self.ID} ")


