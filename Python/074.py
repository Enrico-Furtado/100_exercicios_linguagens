'''74 - Crie um programa que vai gerar 5 números aleatórios, e colocar em uma tupla. Depois disso mostre a listagem dos números 
gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint
var = ()
for i in range(0, 5):
    num = randint(0, 100)
    var = () + (num,) 
    if i == 0:
        nova_tupla = () + var
    else: 
        nova_tupla += var
    del(var)

print(nova_tupla)
print(f"O maior número é {max(nova_tupla)}")
print(f"O menor número é {min(nova_tupla)}")
