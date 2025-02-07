'''69 - Faça um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar 
se o usuário quer ou não continuar. No final mostra: A) quantas pessoas tem mais de 18 anos . B) quantos homens foram cadastrados. 
C) quantas mulheres possuem menos de 20 anos.'''

m_vinte, h, m_dezoito = 0, 0, 0

while True:
    sex = str(input("Digite o sexo da pessoa [M|F]: ")).lower()
    idade = int(input("Digite a idade da pessoa: "))
    if idade > 18:
        m_dezoito += 1
    if sex == 'f' and idade < 20:
        m_vinte += 1
    elif sex == 'm':
        h += 1
    conti = str(input("Você gostaria de continuar cadastrando pessoas? [S|N]\n")).lower()
    if conti == 's':
        print("Vamos continuar a cadastrar!")
    else:
        break

print(f"Dos cadastrados, {m_dezoito} possuem mais de 18 anos,\n {h} são homens e {m_vinte} são mulheres abaixo dos 20 anos.")