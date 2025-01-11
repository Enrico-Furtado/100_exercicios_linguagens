'''33 - Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.'''

print('Digite 3 números abaixo e veremos qual é o maior e o menor!')
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
n3 = int(input('Digite o terceiro número:'))
lista = [n1, n2, n3]
print('O maior número foi', max(lista), 'e o menor foi', min(lista))