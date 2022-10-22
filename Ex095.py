#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = dict()
partidas = list() #vai armazenar os gols de cada partida
time = list()

while True:
    jogador.clear() ## à cada laço vai voltar a ler dados e armazenar no jogador, então ele precisa ser resetado
    jogador['nome'] = str(input('Nome do jogador: ')).strip()
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for i in range(0, total):
        partidas.append(int(input(f'Quantos gols fez na partida {i}? ')))
    jogador['gols'] = partidas[:] ## vai pegar a lista de gols por partida, e salvar uma cópia no atributo gols do dicionário
    jogador['total'] = sum(partidas) ##adiciona uma variável total dentro do dicionario, com a soma dos gols das partidas
    time.append(jogador.copy()) #Copia os dados do jogador(dicionario) e armazena com o append na lista time
    while True:
        opcao = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
        if opcao in 'SN':
            break
        print('ERRO! Digite apenas uma opção válida[S/N]!')
    if opcao == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-='*30)
for k, v in enumerate(time): ##Como time é uma lista, usa o enumerate
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*30)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f'  LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-=' * 30)
