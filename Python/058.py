'''58 - Melhore o jogo do desafio 028 onde o computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai tentar 
adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint

cont = 0
while True:
    numc = randint(0, 10)
    numj = int(input('O computador pensou em um número entre 0 e 10, qual será esse número? '))
    if numj == numc:
        print(f'Parabéns, você acertou!')
        break
    else:
        print(f'Sinto muito, você errou, o número correto é {numc}.')
        cont += 1
print(f'Você precisou de {cont} tentativas para acertar!')