'''Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e último nome separadamente.
Ex: Ana Maria de Souza - Primeiro nome: Ana - Último nome: Souza'''

nome = str(input("Digite o nome completo de uma pessoa: ")).strip().title()
nomes = nome.split()
print("O primeiro nome da pessoa é:",nomes[0])
print("O último nome da pessoa é:",nomes[-1])