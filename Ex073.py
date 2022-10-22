#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético',
         'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

for t in times:
    print(f'{t}', end=' ')

#print(f'Os cinco primeiros colocados são: {times[0:5]}') É a outra forma mais simples que também funciona
print('_'*40)
print('\nOs cinco primeiros colocados são: ')
for i in range(0, 6):
    print(f'{times[i]}', end=' ')

#print(f'Os quatro últimos colocados são: {times[-4:]}') É a outra forma mais simples que também funciona
print('\n\nOs quatro últimos colocados são: ')
for j in range(len(times)-4, len(times)):
    print(f'{times[j]}', end=' ')

times2 = sorted(times) ## Só pra deixar melhor visualmente, fazendo uma variável separada pra ordenar
print('\n\nTimes em ordem alfabética: ')
for ordenados in times2:
    print(f'{ordenados}', end=' ')

##Como a posição da Chapecoense na tupla é 7, e a tupla começa em 0, a Chapecoense está em 8º no campeonato, portanto o +1 no print
print(f'\n\nA Chapecoense está na {times.index("Chapecoense")+1}ª posição.')