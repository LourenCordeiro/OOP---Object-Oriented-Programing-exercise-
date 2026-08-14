from cafeteria import *

def main():
    bebida = Leite()
    bebida.preparar()

    bebida = Cha()
    bebida.preparar()

    bebida = Leite()
    bebida.preparar()


if __name__ == "__main__":
    main()