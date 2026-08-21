from termostato import *
from rich import inspect

def main():
    t = Termostato()
    try:
        t.temperatura = 22.2
    except Exception as e:
        print(f"Houve um problema: {e}")

    print(f"A temperatura atual é de {t.ftemperatura}")

    #inspect(t1, private=True)



if __name__ == '__main__':
    main()