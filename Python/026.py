'''Faça um programa que leia uma frase pelo teclado e mostre: 1 - Quantas vezes aparece a letra 'A'.
2 - Em que posição ela aparece a primeira vez. 3 - Em que posição ela aparece a última vez.'''

frase = str(input("Digite uma frase: ")).strip().upper()
print(f"A letra 'A' apareceu", frase.count('A'), 'vezes.')
print(f"A primeira aparição de 'A' é na posição:", frase.find('A')+1)
print(f"A última aparição de 'A' é na posição:", frase.rfind('A')+1)