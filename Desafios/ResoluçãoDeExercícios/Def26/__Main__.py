from funcionarios import Horista, Mensalista 
from rich import print
from rich import inspect

def main():
    f1 = Horista("Paulo", 12, 200)
    f1.calcular_salario()
    f1.analisar_salario()

    f2 = Mensalista("Amanda", 9000)
    f2.calcular_salario()
    f2.analisar_salario()


if __name__== "__main__":
    main()