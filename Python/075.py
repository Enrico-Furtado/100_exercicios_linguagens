'''75 - Desenvolva um programa que leia 4 valores no teclado, e guarde-os em uma tupla. No final mostre: 
A - Quantas vezes apareceu o valor 9. B - Em que posição foi digitado o primeiro valor 3. C - Quais foram os números pares.'''

tupla = ()
for i in range(0, 4):
    num = int(input("Digite um número inteiro qualquer."))
    if i == 0:
        nova_tupla = () + (num,)
    else:
        nova_tupla += (num,)

pares = 0
for i in nova_tupla:
    if i % 2 == 0:
        pares += 1

print(nova_tupla)
print(f"O valor 9 apareceu {nova_tupla.count(9)} vezes.")
print(f"O primeiro valor 3 foi digitado na posição {nova_tupla.index(3)}")
print(f"Os números pares foram {pares}.")

