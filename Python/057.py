'''57 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação corretamente até ter um valor correto.'''

sexo = ""
while sexo == "":
    sexo = str(input("Digite o sexo da pessoa: [M/mulher] ou [F/homem]")).lower()
    if sexo in 'mf':
        print(f"O sexo da pessoa é {sexo}.")
    else:
        print("Infelizmente você não digitou o valor correto, tente novamente.")
        sexo = ""