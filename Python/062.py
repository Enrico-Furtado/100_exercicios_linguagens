'''62 - Melhore o desafio 061 perguntando ao usuário se ele quer mostrar mais alguns termos. 
O programa encerra quando ele disse que quer mostrar 0 termos.'''

print("Vamos criar uma PA de 10 termos.")
termo = int(input("Diga o primeiro termo: "))
razao = int(input("Diga a razão entre os termos: "))
cont = 0
while cont < 10:
    print(termo, end=" ")
    termo += razao
    cont +=1
while True:
    more = int(input("\nVocê gostaria de mostrar mais quantos termos?\n"))
    if more == 0:
        print("Saindo so programa...")
        break
    else:
        for i in range(0, more):
            print(termo, end=" ")
            termo += razao