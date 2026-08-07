from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo, total_paginas):
        self.titulo = titulo
        self.total_paginas = total_paginas
        self.pagina_atual = 1

        print(
            f":open_book: [blue]Você acabou de abrir o livro '[/][red]{self.titulo}[/][blue]' que tem [/][green]{self.total_paginas} páginas [/][blue]no\n"
            f"total. Você agora está na[/][blue] [yellow]página {self.pagina_atual}[/]"
        )


    def avancar_paginas(self, quantidade):
        pagina_inicial = self.pagina_atual
        self.pagina_atual += quantidade

        chegou_ao_final = self.pagina_atual > self.total_paginas
        if chegou_ao_final:
            self.pagina_atual = self.total_paginas
        
        for pagina in range(pagina_inicial + 1, self.pagina_atual + 1):
            print(f":arrow_forward: Pág{pagina}", end=" ", flush=True)
            sleep(0.5)

        avanco_real = self.pagina_atual - pagina_inicial
        print(f"[blue]Você avançou {avanco_real} páginas e agora está na[/][yellow] página {self.pagina_atual}[/]")

        if chegou_ao_final:
            print(f":rotating_light: [red]Você chegou ao final do livro '{self.titulo}'[/]")
            
     

l1 = Livro("10 coisas que aprendi", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(50)


#Na aula de correção o professor usou o seguinte método

#from rich import print
#import time

#class Livro:
#    def __init__(self, titulo, paginas):
#        self.titulo = titulo
#        self.total_paginas = paginas
#        self.pagina_atual = 1

#        print(f":open_book: [blue]Você acabou de abrir o livro '[red]{self.titulo}[/]' que tem [green] {self.total_paginas} páginas[/] no total. Você agora está na [yellow]página {self.pagina_atual} [/][blue]")

#    def avancar_paginas(self, qtd=1):
#        cont = 0
#        for pg in range(0, qtd, 1):
#            if not self.fim_do_livro():
#                self.pagina_atual += 1
#                print(f"Pág{self.pagina_atual} :arrow_forward: ", end='')
#                time.sleep(0.3)
#                cont += 1
        
#        print(f"[blue] Você avançou {cont} páginas e agora está na [yellow]página {self.pagina_atual}[/][/blue]")
#        if self.fim_do_livro():
#            print(f":closed_book: [red]Você chegou ao fim do livro '{self.titulo}'[/red]")

#    def fim_do_livro(self) -> bool:
#        return True if self.pagina_atual == self.total_paginas else False


#l1 = Livro("10 coisas que aprendi", 20)
#l1.avancar_paginas(5)
#l1.avancar_paginas(10)
#l1.avancar_paginas(50)