#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista.
# No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

pessoa = dict()
galera = list()
soma = media = 0

while True:
    pessoa.clear() ##Limpar o dicionario pessoa
    #recebendo os valores nome, sexo, idade
    pessoa['Nome'] = str(input('Nome: ')).strip()
    #Verificando se a pessoa digita corretamente o Sexo, somente com M ou F
    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        else:
            print('Por favor, digite uma opção válida[M/F]!')
    pessoa['Idade'] = int(input('Idade: '))
    #Soma recebe a idade como incremento
    soma += pessoa['Idade']
    galera.append(pessoa.copy()) #A lista galera recebe(ou seja, é um append) uma cópia do dicionário pessoa(cópia de dicionário somente com .copy())

    #Verificando a opção do usuário de continuar ou não no programa
    while True:
        opcao = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if opcao in 'SN':
           break
        print('Erro! Responda apenas [S/N]!')
    if opcao == 'N':
        break
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos.') ##média será mostrada com 5 casas, e 2 decimais
print('As mulheres cadastradas foram: ', end='')
for i in galera:
    if i['Sexo'] in 'F':
        print(f'{i["Nome"]}', end='...')
print()
print(f'A listas das pessoas que estão acima da média: ', end='')
for j in galera:
    if j['Idade'] >= media:
        print(f'{i["Nome"]}', end='...')
print('\n<<< ENCERRADO >>>')