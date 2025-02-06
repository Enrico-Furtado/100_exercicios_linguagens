'''60 - Faça um programa que leia um número qualquer e mostre o seu fatorial.'''
fact = 1
num = int(input("Digite um número e iremos calcular o seu fatorial!"))
for i in range(num, 0, -1):
    fact *= i
print(f'O fatorial de {num} é {fact}')   