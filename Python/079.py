'''79 - Crie um programa onde o usuário pode digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro ele não será adicionado. No final serão exibidos todos os valores únicos digitados em ordem crescente.'''

lista = []

while True:
    valor = float(input("Digite um valor numérico: "))
    if valor in lista:
        print("Você já inseriu esse valor, tente outro.")
    else:
        lista.append(valor)
    res = input("Gostaria de parar de inserir valores? [S|N]")
    if res in 'Nn':
        break
lista.sort()
print(f"Os valores digitados em ordem numérica são {lista}")
    