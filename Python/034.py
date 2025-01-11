'''34 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salário superiores a 1250 reais, calcule um aumento de 10%. Para inferiores ou iguais, o aumento é de 15%.'''

sal = float(input('Qual é o salário do funcionário? '))
if sal <= 1250:
    aumento = 1.15 * sal
else: 
    aumento = 1.1 * sal

print(f'O salário foi aumentado e seu valor atual é de: R${aumento:.2f}.')