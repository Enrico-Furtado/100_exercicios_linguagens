'''55 - Faça um programa que leia o peso de 5 pessoas. No final mostre qual foi o maior e o menor peso lidos.'''
menor = 0
maior = 0
for i in range(1, 6):
    peso = float(input(f"Digite o peso da {i} pessoa: "))
    if i == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso foi de {maior}Kg e o menor peso foi {menor}Kg.')