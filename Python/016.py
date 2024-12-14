'''16 - Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.'''
from math import trunc
num = float(input('Digite qualquer número real: '))
inte = trunc(num)
print(f'A parte inteira do número é {inte}.')


"""
real = float(input('Digite qualquer número real: '))
print(f'A parte inteira do número é {real:.0f}.')
"""