from rich import print, inspect
from poligono import Quadrado, Circulo


def main():
    q = Quadrado(20)
    print(f"Um quadrado de lado {q.lado}cm tem perímetro de {q.perimetro()}cm")
    print(f"Um quadrado de lado {q.lado}cm tem área de {q.area()}cm2")


    c = Circulo()
    print(f"Um círculo de lado {c.raio}cm tem perímetro de {c.perimetro():.1f}cm")
    print(f"Um círculo de lado {c.raio}cm tem área de {c.area():.1f}cm2")



if __name__ == "__main__":
    main()

