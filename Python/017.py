'''17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.'''

cato = float(input('Digite o comprimento do cateto oposto em cm: '))
cata = float(input('Digite o comprimento do cateto adjacente em cm: '))
hipo = (cato ** 2 + cata ** 2) ** (1/2)
print(f'O comprimento da Hipotenusa é: {hipo:.2f}cm.')


"""
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa do triângulo é {:.2f}'.format(hi))
"""