# EXERCÍDIO 6 - Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e a sua raíz quadrada.

num = float(input('Digite um número: '))
dob = num * 2
trip = num * 3
raiz = num ** (1/2)

print(f'O dobro de {num} é {dob}, seu triplo é {trip} e sua raíz quadrada é {raiz}.')