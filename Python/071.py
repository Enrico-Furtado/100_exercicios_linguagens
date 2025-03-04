'''71 - Crie um programa que simule o funcionamento de um caixa eletrônico. No início pergunte ao usuário qual o valor a ser sacado 
(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: Considere que o caixa possui cédulas 
de 50, 20, 10, 1 real.'''

ced_50, ced_20, ced_10, ced_1 = 0, 0, 0, 0
atual = 0

while True:
    valor = int(input("Qual o valor você gostaria de sacar?"))
    ced_50 = valor // 50
    atual = valor % 50
    ced_20 = atual // 20
    atual = atual % 20
    ced_10 = atual // 10
    atual = atual % 10
    ced_1 = atual // 1
    atual = atual % 1
    print(f'Você está recebendo {ced_50} cédulas de 50, {ced_20} cédulas de 20, {ced_10} cédulas de 10 e {ced_1} cédulas de 1 real.')
    saque_mais = input("Você gostaria de sacar mais?[S|N]")
    if saque_mais not in 'Ss':
        break