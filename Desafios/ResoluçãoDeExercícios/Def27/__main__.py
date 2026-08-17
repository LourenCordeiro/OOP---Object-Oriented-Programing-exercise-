from personagem_rpg import *
from rich import inspect

def main():
    p1 = Guerreiro("Kitsune", 1000)
    p2 = Mago("Gadalf", 900)

    p1.atacar(p2, 200)    
    p2.atacar (p1)
    p1.curar()
    p2.curar()

    p1.status_jogo(p2)



    #inspect(p1, methods=True)


if __name__ == "__main__":
    main()