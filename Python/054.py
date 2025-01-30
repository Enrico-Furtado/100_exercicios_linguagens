'''54 - Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade 
e quantas já são maiores.'''
from datetime import date
totmai = 0
totmen = 0
for i in range(1, 8):
    nasc = int(input(f'Qual é o ano de nascimento da {i} pessoa? '))
    idade = date.today().year - nasc
    if idade >= 18:
        totmai += 1
    else:
        totmen += 1

print(f'No total, {totmai} pessoas são maiores de idade e {totmen} menores de idade.')