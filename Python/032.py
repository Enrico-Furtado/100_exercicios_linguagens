'''32 - Faça um programa que leia um ano quaquer e mostre se ele é bissexto.'''

ano = int(input('Digite um ano qualquer e vamos verificar se ele é bissexto: '))
if ano % 4 == 0 or ano % 400 == 0:
    print(f'O ano é bissexto!')
else:
    print(f'O ano não é bissexto!')