'''Crie um programa que leia o nome completo de uma pessoa e mostre: 1 - O nome com todas as letras maiúsculas. 
2 - O nome com todas minúsculas. 3 - Quantas letras ao todo (sem considerar espaços). 4 - Quantas letras tem o primeiro nome.'''

nome = str(input('Digite o seu nome completo: ')).strip()
nup = nome.upper()
nlow = nome.lower()
nsplit = nome.split()
nlen = int(len(nsplit[0])) + int(len(nsplit[1]))
nfirst = int(len(nsplit[0]))
print(f'O nome com todas as letras maiúsculas é {nup}.')
print(f'O nome com todas as letras minúsculas é {nlow}.')
print(f'O total de letras nesse nome sem considerar espaços é de {nsplit}.')
print(f'O primeiro nome possui {nfirst} letras.')
