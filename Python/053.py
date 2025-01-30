'''53 - Crie um programa que leia uma frase qualquer e diga se é um palíndromo desconsiderando os espaços.'''

print("Vamos ver se sua frase é um palíndromo:")
frase = str(input("Escreva sua frase: ")).lower().split()
print(frase)
frase_2 = "".join(frase)
inverso = ""
for i in range(1, len(frase_2) + 1):
    inverso += frase_2[-i]

if frase_2 == inverso:
    print("É um PALÍNDROMO!")
else:
    print("NÃO É UM PALÍNDROMO!")