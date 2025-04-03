'''78 - Faça um programa que leia 5 valores numéricos e guarde numa lista. No final mostre qual foi o maior e o menor valor digitados 
e as suas respectivas posições na lista.'''

lista = []
maior, menor = 0, 0

for c in range(0, 5):
    n = int(input("Digite um valor inteiro: "))
    lista.append(n)
    if len(lista) == 1:
        maior = lista[c]
        menor = lista[c]
    elif lista[c] < lista[c-1]:
        menor = lista[c]
    elif lista[c] > lista[c-1]:
        maior = lista[c]

print(f"O maior número é {maior}.")
print(f"O menor número é {menor}")
        



#print(f"O maior número dentro da lista é {max(lista)}")
#print(f"O menor número dentro da lista é {min(lista)}")