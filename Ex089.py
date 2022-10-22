#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista = list()

while True:
    #Recebendo os valores e armazenando na lista como um único item
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    #As notas vão entrar como um único elemento dentro da lista
    lista.append([nome, [nota1, nota2], media])

    #Verificando se o usuário deseja continuar no programa
    opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break
print('=-'*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
('__'*30)
for i, j in enumerate(lista): ##i = posição // j = elemento
    print(f'{i+1:<4}{j[0]:<10}{j[2]:>8.1f}') ##Não quero mostrar o aluno como aluno 0, então vou adicionar 1 ao i=posição

while True:
    ('__' * 30)
    op = int(input('Mostrar a nota de qual aluno? (999 interrompe): '))
    if op == 999:
        break
    #Se a opção digitada estiver dentro do range de indices da lista, ele exibe
    if op <= len(lista):
        ##lista[no aluno que o usuário quer][na posição do nome do aluno]
        print(f'Notas de {lista[op-1][0]} são {lista[op-1][1]}') ##Como o usuário está vendo posição+1,é necessário tirar 1 pra pegar a opção certa, portanto 0p-1
print('ENCERRANDO O PROGRAMA...')