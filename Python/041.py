'''41 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria 
de acordo com a sua idade. Até 9 anos: MIRIM. Até 14 anos: INFANTIL. Até 19 anos: JUNIOR. Até 25 anos: SÊNIOR. Acima: MASTER.'''
from datetime import date

nasc = int(input("Qual o ano de nascimento do atleta? "))
today = date.today().year
idade = today - nasc
print("A categoria do atleta é: ")
if idade <= 9:
    print("MIRIM")
elif 9 < idade <=14:
    print("INFANTIL")
elif 14 < idade <= 19:
    print("JUNIOR")
elif 19 < idade <= 25:
    print("SÊNIOR")
else:
    print("MASTER")
