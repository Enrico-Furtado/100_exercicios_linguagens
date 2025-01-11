''' 31 - Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando 0,50 centavos por 
KM para viagens de até 200KM e R$0,45 para viagens mais longas. '''

dist = float(input('Qual a distância da viagem em Km?'))
preco = 0
if dist <= 200:
    preco = dist * 0.5
    print(f'Para esta viagem, o preço será de R${preco}.')
else:
    preco = dist * 0.45
    print(f'Para esta viagem, o preço será de R${preco}.')