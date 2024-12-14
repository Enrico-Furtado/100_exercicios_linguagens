'''19 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.'''

import random
a1 = str(input('Nome do primeiro aluno: '))
a2 = str(input('Nome do segundo aluno: '))
a3 = str(input('Nome do terceiro aluno: '))
a4 = str(input('Nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
ordem = random.shuffle(lista)
print(f'A ordem de apresentação é {ordem}.')