'''80 - Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

lista = []
cont = 0
maior  = 0
menor = 0

while cont < 5:
    valor = int(input("Digite um número inteiro e vamos cadastrá-lo em uma lista: "))
    if len(lista) == 0:
        lista.append(valor)
        maior = valor
        menor = valor
    elif valor > maior:
        maior = valor
        lista.append(valor)
    elif valor < menor:
        menor = valor
        lista.insert(0, valor)
    elif valor in lista:
        lista.insert(lista.index(valor), valor)
    else:
        for i in range(0, len(lista)):
            if valor < lista[i]:
                lista.insert(i, valor)
                break
            elif valor > lista[i]:
                lista.insert(i, valor)
                break
    cont += 1

print(lista)

