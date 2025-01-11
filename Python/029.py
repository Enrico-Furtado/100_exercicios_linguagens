'''Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80km\h mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 pra cada KM acima do limite.'''

vel = float(input('Digite a velocidade do carro em Km/h: '))
if vel > 80:
    print('Sua velocidade é maior o que a permitida!')
    print('VOCÊ SERÁ MULTADO!')
    multa = (vel - 80) * 7
    print(f'Sua multa será de R${multa}.')
else:
    print('Parabéns, você está dentro do limite de velocidade.')