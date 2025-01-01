'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos quatro dígitos separados.'''

num = int(input("Digite um número entre 0 e 9999: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"Unidade é: {u}.")
print(f"Dezena é: {d}.")
print(f"Centena é: {c}.")
print(f"Milhar é: {m}.")

'''
O código abaixo apenas funciona se o usuário digitar um número de 4 dígitos.
num = str(input("Digite um número inteiro entre 0 e 9999: "))
print(f"O algarismo das unidades é {num[-1]}")
print(f"O algarismo das dezenas é {num[-2]}.")
print(f"O algarismo das centenas é {num[-3]}.")
print(f"O algarismo dos milhares é {num[-4]}.")
'''