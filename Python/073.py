'''73 - Crie uma tupla preenchida com com 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação, 
depois mostre: A- Apenas os primeiros colocados. B - Os últimos 4 colocados da tabela. C - Uma lista com os times em ordem alfabética. 
D - Em que posição da tabela está o Cruzeiro.'''

tabela = ("Botafogo", "Palmeiras", "Flamengo", "Fortaleza", "Internacional", "São Paulo", "Corinthians", "Bahia", "Cruzeiro", "Vasco", "Vitória", "Atlético-MG", "Fluminense", "Grêmio", "Juventude", "Red Bull Bragantino", "Athletico", "Criciúma", "Atlético-GO", "Cuiabá")

print(f"Os primeiros colocados da tabela são {tabela[0:3]}")
print(f"Os últimos 4 colocados da tabela são {tabela[-4:]}")

lista = []
for t in range(0, len(tabela)):
    lista.append(tabela[t])


print(f'A lista de colocados em ordem alfabética é {sorted(lista)}')
print(f'O Cruzeiro está na {tabela.index("Cruzeiro")} posição da tabela.')