'''52 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

print("Digite um número e veremos se ele é primo:")
num = int(input("Digite o número: "))
c = 0
for i in range (2, num):
    print(i)
    if num % i == 0:
        c = 1

if c == 1:
    print("O número não é primo!")
else:
    print("O número É PRIMO!")