''' 12 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto. '''
preco = float(input('Qual é o preço do produto? '))
desc = 0.95 * preco
print(f'O preço do produto com 5% de desconto é R$ {desc:.2f}.')