'''67 - Faça um programa que mostre a tabuada de vários números. Um de cada vez para cada valor digitado pelo usuário. 
O programa será interrrompido quando o número solicitado for negativo.'''


while True: 
    num = int(input('Digite um numero inteiro qualquer: '))
    if num < 0:
        break
    print(f'A tabuada de {num} é: ')
    print('||','-'*12,'||')
    for i in range(1, 11):
        print(f'{num} x {i} = {num*i}')
    print('-'*12)