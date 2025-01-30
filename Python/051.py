'''51 - Desenvolva um programa que leia o primeiro termo e a razão de um PA. No final mostre os 10 primeiros termos dessa progressão.'''

print("Vamos criar uma PA de 10 termos.")
termo = int(input("Diga o primeiro termo: "))
razao = int(input("Diga a razão entre os termos: "))
for i in range(0, 10):
    print(termo, end=" ")
    termo += razao

