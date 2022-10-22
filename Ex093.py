#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
partidas = list() #vai armazenar os gols de cada partida

jogador['nome'] = str(input('Nome do jogador: ')).strip()
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(0, total):
    partidas.append(int(input(f'Quantos gols fez na partida {i}? ')))
    jogador['gols'] = partidas[:] ## vai pegar a lista de gols por partida, e salvar uma cópia no atributo gols do dicionário
    jogador['total'] = sum(partidas) ##adiciona uma variável total dentro do dicionario, com a soma dos gols das partidas
print('-='*30)
for k, v in jogador.items():
    print(f'{k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(partidas)} partidas e marcou {jogador["total"]} gols.')