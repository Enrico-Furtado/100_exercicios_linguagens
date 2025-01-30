'''49 - Refaça o desafio 009 mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço FOR.'''

num = int(input('Digite um numero inteiro qualquer: '))
print(f'A tabuada de {num} é: ')
print('||','-'*12,'||')
for i in range(1, 11):
    print(f'{num} x {i} = {num*i}')
print('-'*12)

