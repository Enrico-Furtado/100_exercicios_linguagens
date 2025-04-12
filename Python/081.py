'''81 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre: 
A-> Quantos números foram digitados. B-> A lista de valores ordenada na ordem decrescente. 
C-> Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
maior = 0
menor = 0
cont = 0

while True:
    valor = int(input("Digite uma valor e ele será colocado em uma lista: "))
    if len(lista) == 0:
        lista.append(valor)
        menor = valor
        maior = valor
    resp = input("Você quer parar de digitar valores? [S|N]")
    if resp in 'Nn':
        break
    
    elif valor > maior:
        lista.insert(0, valor)
        maior = valor
    elif valor < menor:
        lista.append(valor)
        menor = valor
    elif valor in lista:
        lista.insert(lista.index(valor), valor)
    else:
        for p in lista:
            if valor < lista[p]:
                lista.insert(p + 1, valor)
                break
            else:
                lista.insert(p, valor)
                break
        

print(f"O total de números digitados foi {len(lista)}")
print(lista)
print("O valor 5 foi digitado na lista") if 5 in lista else print("O valor 5 não foi digitado na lista.")