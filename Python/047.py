'''47 - Crie um programa que mostre na tela todos os números pares que que estão no intervalo entre 1 e 50.'''

print("Os números pares de 1 até 50 são:")
for i in range(1, 51):
    if i % 2 == 0:
        print(f"{i}", end =" ")