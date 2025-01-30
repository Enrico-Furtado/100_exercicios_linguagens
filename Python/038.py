'''38 - Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem. 
- O primeiro valor é maior. O segundo valor é maior. Não existe valor maior, os dois são iguais.-'''

print("Digite dois números inteiros e veremos qual deles é o maior.")
num1 = int(input("Digite o primeiro número: \n"))
num2 = int(input("Digite o segundo número: \n"))
if num1 == num2:
    print("Não existe valor maior, os dois são iguais.")
elif num1 > num2:
    print("O primeiro valor é maior.")
else:
    print("O segundo valor é maior.")