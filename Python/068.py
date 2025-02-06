'''68 - Faça um programa que leia par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint
parip = ""
paric = ""
vit = 0
print("Vamos jogar par ou ímpar com o computador!")
while True:
    resp = str(input("Você escolher PAR ou ÍMPAR? [P|I]")).upper()
    if resp not in "PI":
        print("Você não deu uma resposta válida, vamos tentar novamente?")
    else:
        while True:
            num = int(input("Qual número de 0 a 10 você escolher? "))
            if num not in range(0,11):
                print("Você colocou um número além dos limites estabelecidos, vamos tentar novamente?")
            else:
                break 
    if resp == 'P':
        parip = 'PAR'
        paric = 'ÍMPAR'
    else:
        parip = 'ÍMPAR'
        paric = 'PAR'
    rand_n = randint(0, 10)
    soma = rand_n + num
    if resp == 'P' and soma % 2 == 0:
        print(f"O computador escolheu {paric} e você escolheu {parip}")
        print(f"O computador escolheu o número {rand_n} e você escolheu o número {num}.")
        print(f"A soma dos dois números deu {soma}.")
        print(f'Você GANHOU!')
        vit += 1
    elif resp == 'I' and soma % 2 != 0: 
        print(f"O computador escolheu {paric} e você escolheu {parip}")
        print(f"O computador escolheu o número {rand_n} e você escolheu o número {num}.")
        print(f"A soma dos dois números deu {soma}.")
        print(f'Você GANHOU!')
        vit += 1
    else:
        print(f"O computador escolheu {paric} e você escolheu {parip}")
        print(f"O computador escolheu o número {rand_n} e você escolheu o número {num}.")
        print(f"A soma dos dois números deu {soma}.")
        print(f'Você PERDEU!')
        print(f"No total você ganhou {vit} vezes seguidas!")
        break