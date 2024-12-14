'''18 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''
from math import sin, tan, cos, radians
angulo = float(input('Digite um ângulo aleatório: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O seno é {seno:.2f}, o cosseno é {cosseno:.2f} e a tangente é {tangente:.2f}.')