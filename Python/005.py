# Exercício 5 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Escreva um número inteiro: '))
ant = num - 1
suc = num + 1

print(f'O sucessor do número {num} é {suc} e seu antecessor é {ant}.')