'''76 - Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência. 
No final mostre uma listagem de preços organizando os dados em forma tabular.'''

tupla = ("caneta",0.50,"caderno",10,"borracha",1)

print("-"*40)
print("Lista de Preços")
print("-"*40)
for pos in range (0, len(tupla)):
    if pos % 2 == 0:
        print(f"R$ {tupla[pos]:.<30}", end = " ")
    else:
        print(f"R$ {tupla[pos]:.2f}")
print("-"*40)