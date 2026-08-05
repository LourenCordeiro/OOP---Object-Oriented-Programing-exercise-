from rich.traceback import install
install()
#O comando install() vai instalar o Rich Traceback, que é uma biblioteca que permite exibir tracebacks de forma bem detalhada e visualmente atraente, ou seja,
#vai exidir o que tem de errado em um programa, para que possamos corrigir o erro.

def divisão(x, y):
    return x/y


print(divisão(50, 0))