'''65 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e 
qual foi o maior e menor valores lidos. O programa deve perguntar ao usuário se ele deve ou não continuar a digitar valores.'''
cont, soma, s, maior, menor = 0, 0, 0, 0, 0
while s == 0:
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    media = soma / cont
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    while True:
        cond = str(input('Você gostaria de digitar mais valores? [S/N]')).upper()
        if cond != 'S':
            s = 1
            break
        else:
            break   
print(f'A média é {media}.')
print(f'O menor número digitado foi {menor} e o maior foi {maior}.')