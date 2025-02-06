'''64 - Crie um programa que leia vários números inteiros pelo teclado. O progama só pode parar quando o usuário digitar o valor 999, 
que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles. (desconsiderando o flag)'''
cont = 0
soma = 0 
print("Digite números e no final veremos quantos números foram digitados \ne qual é a soma entre eles.")
while True:
    num = int(input("Digite o número [999 para parar]: "))
    if num == 999:
        break
    soma +=num
    cont +=1
print(f'Você digitou {cont} números.')
print(f'A soma entre os números foi de {soma}.')
