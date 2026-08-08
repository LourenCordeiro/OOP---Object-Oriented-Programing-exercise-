from rich import print
from rich.panel import Panel

class ControleRemoto:
    #definição de atributos de classe
    canal_min:int = 1
    canal_max:int = 5
    volume_min:int = 1
    volume_max:int = 5

    def __init__(self, canal=1, volume=2):
        #definição de atributos de instância
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False

    def liga_desliga(self):
        self.ligado = not self.ligado       #nesse caso se inicia como False vira True e se inicia True vira False (sem necessidade de uso do "if")

    def canal_mais(self):                                       #Adiciona o comportamento circular da mudança de canal de uma TV 
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1

    def canal_menos(self):                  
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1

    def volume_mais(self):                      #comportamento diferente do canal, nesse caso o volume quando no máx ou no mín fica estacionado
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_max:
                self.volume_atual += 1
    
    def volume_menos(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_min:
                self.volume_atual -= 1
                
    def mostrar_tv(self):
        conteudo = ''
        if not self.ligado:
            conteudo = f":prohibited: [red]A TV está desligada[/]"
        else:
            conteudo = f"CANAL = "
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):         #esse "for" fará o canal "acender" de acordo com o que for selecionado
                if canal == self.canal_atual:
                    conteudo += f"[yellow on yellow] {canal} [/]"
                else:
                    conteudo += f" {canal} "
            
            conteudo += f"\nVOLUME = "                                                          #esse for fará a barra de volume se preenchida de acordo com o selecionada
            for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max + 1):
                if volume <= self.volume_atual:
                    conteudo += "[black on cyan] [/]"
                else:
                    conteudo += "[black on white] [/]"

        tv = Panel(conteudo, title="[ TV ]", width=30)
        print(tv)

c = ControleRemoto()
while True:
    c.mostrar_tv()
    comando = str(input(f"< CH{c.canal_atual} >   - VOL{c.volume_atual} + "))
    match comando:
        case '0':
            break
        case '@':
            c.liga_desliga()
        case '>':
            c.canal_mais()
        case '<':
            c.canal_menos()
        case '-':
            c.volume_menos()
        case '+':
            c.volume_mais()
    print("\n" * 10)
