'''37 - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão.
1- Para Binário. 2 - Para Octal. 3 - Para hexadecimal.'''

num = int(input("Digite um número inteiro qualquer: "))
base = int(input("Agora digite a base de conversão: 1 - Binário , 2 - Octal. 3 - Hexadecimal."))
bina = bin(num)
octa = oct(num)
hexa = hex(num)
if base == 1:
    print(f"O número convertido para binário é {bina}")
elif base == 2:
    print(f"O número convertido para binário é {octa}")
elif base == 3:
    print(f"O número convertido para binário é {hexa}")