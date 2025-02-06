'''Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça 
para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint

numc = randint(0, 5)
numj = int(input('O computador pensou em um número entre 0 e 5, qual será esse número? '))
if numj == numc:
    print(f'Parabéns, você acertou!')
else:
    print(f'Sinto muito, você errou, o número correto é {numc}.')
