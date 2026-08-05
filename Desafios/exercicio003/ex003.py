class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, ID, nome, saldo =0):
        self.ID = ID
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.ID} criada com sucesso. Saldo atual de R${self.saldo:.2f}")


    def __str__(self):
        return f"A conta {self.ID} de {self.titular} tem R${self.saldo:.2f} de saldo."


    def depositar (self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} autorizado na conta {self.ID} ")


    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque NEGADO de R$ {valor:,.2f} na conta {self.ID}: SALDO INSUFICIENTE")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} autorizado na conta {self.ID} ")


nome = (input('Informe o nome do Titular: '))
ID = int(input('Insira o ID: '))
saldo = int(input('Informe o saldo: '))
c1 = ContaBancaria (ID, nome , saldo)

c1.depositar(500)
c1.sacar(2_000_000)
print(c1)