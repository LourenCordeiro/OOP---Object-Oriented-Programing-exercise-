#from rich import print

#print ("Olá [red]Mundo[/]! :earth_americas:")
#print ("Boa Noite!")

import random
nums = random.choices(range(10), k=4)
print(nums)

vistos = []
tem_repetido = False

for numero in nums:
    if numero in vistos:
        tem_repetido = True
    vistos.append(numero)

if tem_repetido:
    print("True")
else:
    print("False")
