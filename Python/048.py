'''48 - Faça um programa que calcule a soma entre todos os números ímpares que são múltiploes de 3 e que se encontram no intervalo 
de 1 até 500.'''

print("Todos os números ímpares múltiplos de 3 no intervalo de 1 até 500 são:")
soma = 0
for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        print(i, end=" ")
        soma += i
print(f'\nA soma de todos esses números é {soma}.')