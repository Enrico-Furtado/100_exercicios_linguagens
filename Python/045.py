'''45 - Crie um programa que faça o computador jogar jokenpô com você.'''

from random import randint
print("Vamos jogar jokenpô!")
comp = randint(1, 3)
jok = int(input("Faça a sua escolha: \n[1]Pedra\n[2]Papel\n[3]Tesoura\n"))
if jok == comp:
    print("EMPATOU!")
elif (jok == 1 and comp == 3) or (jok == 2 and comp == 1) or (jok == 3 and comp == 2):
    print("Você GANHOU!")
else:
    print("Você PERDEU!")