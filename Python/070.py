'''70 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. 
No final mostre: A) Qual o gasto total da compra. B) Quantos produtos custam mais de R$1000. C) Qual o nome do produto mais barato.'''

soma, p_mil, menor = 0, 0, 0
nome_menor = ""
cont = 0
while True:
    nome = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço do produto: "))
    soma += preco
    cont += 1
    if preco > 1000:
        p_mil += 1
    if cont == 1:
        menor = preco
        nome_menor = nome
    else:
        if preco < menor:
            menor = preco
            nome_menor = nome
    conti = str(input('Gostaria de continuar cadastrando produtos? [S|N]')).lower()
    if conti == 's':
        print("Vamos cadastrar mais um produto!")
    else:
        break
print(f'O gasto total da compra foi de R${soma:.2f}.')
print(f'No total, {p_mil} produtos custaram mais de R$1000,00.')
print(f'O produto mais barato foi {nome_menor}')