from transporte import *
from rich import print
from rich.table import Table


def main():
    dist = 50
   
    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]      #ciado uma lista com as informações de classe para rodar o laço

    tabela = Table(title='Tabela de Fretes')        
    tabela.add_column('Distância', justify='center')
    tabela.add_column('Tipo', justify='center')
    tabela.add_column('Frete', justify='center')

    for item in viagem:         #o laço percorre as classes detro do vetor junto com os items de cada classe, sendo intulidade para serem chamados
        tabela.add_row(f"{dist}Km", f"{type(item).__name__}", f"{item.calcular_frete()}", style='cyan')

    print(tabela)


if __name__ =="__main__":
    main()
