'''59 - Crie um programa que leia dois valores e mostre um menu na tela: 
[1]somar. [2]multiplicar. [3]maior. [4]novos números. [5]sair do programa. 
Seu programa deve realizar a operação solicitada em cada caso.'''

while True:
    v1 = int(input("Primeiro Valor:"))
    v2 = int(input("Segundo Valor: "))
    print("Escolha uma das opções abaixo: \n[1]somar\n[2]multiplicar.\n[3]maior.\n[4]novos números.\n[5]sair do programa.")
    opcao = int(input("Opção: "))
    if opcao == 1:
        print(f'A soma dos dois valores é {v1 + v2}')
    elif opcao == 2:
        print(f'A multiplicação dos dois valores é {v1 * v2}')
    elif opcao == 3:
        print(f'O maior número é {max(v1, v2)}')
    elif opcao == 5:
        print(f'Você saiu do programa.')
        break
    elif opcao == 4:
        print(f'Opa, você quer novos números? Vamos lá!')
    else:
        print(f'Opção inválida, vamos tentar de novo!')