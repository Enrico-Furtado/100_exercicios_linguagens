# EXERCÍCIO 4 - Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input('Escreva alguma coisa: ')
n = input('Escreva algo:')
print('O tipo primitivo desse valor é ', type(n))
print('Só tem espaços? ', n.isspace())
print('É um número? ', n.isnumeric())
print('É alfabético? ', n.isalpha())
print('É alfanumérico? ', n.isalnum())
print('Está em maiúculas? ', n.isupper())
print('Está em minúsuculas?' , n.islower())
print('Está capitalizada?' , n.istitle())

