from exercicio008 import ContaBancaria

def main():
    c1 = ContaBancaria(111, "Maria", 5000)
    c1.depositar(1000)
    c1.sacar(100)
#    c1.titular = "Pedro"    Nessa caso mesmo o nome sendo protegido o python não substitui o Maria mas cria uma variável "Pedro". Se pedir para
#   o c1_titular então o código python irá mudar 
#    c1.__saldo = 0  #Nesse caso que o atributo é private(-) ele continua mantendo o saldo inicial e cria um novo atributo
#    c1._ContaBancaria__saldo = 0 #Nesse caso o saldo mudaria 
    print(c1)



if __name__=="__main__":
    main()