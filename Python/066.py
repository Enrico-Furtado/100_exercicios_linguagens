'''66 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, 
que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles. (Desconsiderando o flag)'''



cont, soma = 0, 0
while True: 
    n = int(input('Digite um número inteiro [999 para para]: '))
    if n == 999:
        break
    cont += 1
    soma += n

print(f'Você digitou {cont} números.')
print(f'A soma de todos esses números é {soma}.')
