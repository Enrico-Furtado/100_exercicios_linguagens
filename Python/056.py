'''56 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre: A média de idade do grupo. 
Qual é o nome do homem mais velho. Quantas mulheres tem menos de 20 anos.'''
mai_idade = 0
n_velho = ""
soma = 0
mulh = 0
hom = 0
mu_subvinte = 0
for i in range (1, 6):
    pes = str(input('A pessoa é homem (H) ou mulher (M)?'))
    nome = str(input(f'Digite o nome da {i} pessoa: '))
    idade = int(input(f"Digite a idade da {i} pessoa: "))
    soma += idade
    media = soma / i
    if pes == 'M':
        mulh += 1
        if idade < 20:
            mu_subvinte += 1 
    elif pes == 'H':
        if i != 1 and idade > mai_idade:
            mai_idade = idade
            n_velho = nome




print(f'A média de idade das pessoas é {media} anos.')
print(f'O nome do homem mais velho é {n_velho}')
print(f'O número de mulheres abaixo de 20 anos é {mu_subvinte}.')
