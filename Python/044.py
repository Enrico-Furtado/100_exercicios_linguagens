'''44 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento. 
- à vista dinheiro/cheque: 10% de desconto. à vista cartão: 5% de desconto. em até 2x no catão: preço normal. 
3x ou mais no cartão: 20% de juros.-'''

print("Vamos calcular o preço do seu produto de acordo com a condição de pagamento.")
preco = float(input("Qual é o preço normal da sua mercadoria: "))
cond = int(input("Escolha sua condição de pagamento: \n[1]À vista dinheiro/cheque: 10% de desconto.\n[2]À vista cartão: 5% de desconto.\n[3]Em até 2x no catão: preço normal.\n[4]3x ou mais no cartão: 20% de juros.\n"))
if cond == 1:
    preco = preco * 0.9
    print(f"O preço final do seu produto é R${preco}.")
elif cond == 2:
    preco = preco * 0.95
    print(f"O preço final do seu produto é R${preco}.")
elif cond == 3:
    print(f"O preço final do seu produto é R${preco}.")
elif cond == 4:
    preco = preco * 1.2
    print(f"O preço final do seu produto é R${preco}.")
else: 
    preco = preco
    print("Condição inválida de pagamento, tente novamente!")
