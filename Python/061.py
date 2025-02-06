'''61 - Refaça o desafio 051 lendo o primeiro termo e a razão de uma PA mostrando os 10 primeiros termos da progressão usando a 
estrutura while.'''

print("Vamos criar uma PA de 10 termos.")
termo = int(input("Diga o primeiro termo: "))
razao = int(input("Diga a razão entre os termos: "))
cont = 0
while cont < 10:
    print(termo, end=" ")
    termo += razao
    cont +=1
