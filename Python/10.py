# EXERCÍCIO 10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere U$$1,00 = R$5,94. (27/11/2024)

cart = float(input('Quantos reais você possui em sua carteira? '))
dol = cart / 5.94

print(f'Com o total de R${cart} você pode comprar US${dol:.2f}.')
