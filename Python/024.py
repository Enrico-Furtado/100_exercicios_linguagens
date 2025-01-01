'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'.'''

#código sem a utilização de condicionais.
from time import sleep
cid = str(input("Digite o nome de uma cidade: ")).strip().upper()
print("O nome desta cidade começa com 'SANTO'?.")
sleep(3)
cids = cid.split()
print('SANTO' in cids[0])

