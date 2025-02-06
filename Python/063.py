'''63 - Escreva um programa que leia um número 'n' inteiro qualquer e mostre na tela os 'n' primeiros elementos de uma sequência de 
Fibonacci.'''

print("Vamos fazer uma sequência de Fibonacci?")
termos = int(input("Insira quantos termos você quer que a sequência possua: "))
fibo1 = 1
fibo2 = 1
cont = 0
print(fibo1, end = " ")
print(fibo2, end = " ")
while cont < termos - 2:
    s = fibo1 + fibo2
    print(s, end= " ")
    fibo1 = fibo2
    fibo2 = s
    cont += 1