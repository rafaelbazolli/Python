#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.

temp = []
princ = []
maior = menor = 0

while True:
    ##Atribuindo os valores na lista temporária
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    #Se não cadastrou ninguém ainda, então o maior e menor serão o que acabou de ser inserido
    if len(princ) == 0:
        ##temp[0] é o nome lido, temp[1] é o peso. Logo, é necessário pegar apenas o temp[1]
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    ##Passando os valores de temp para a principal
    princ.append(temp[:])
    ##Apagando a lista temporária
    temp.clear()

    ##Validando a opção do usuário de continuar no programa ou não
    opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('_'*30)
print(f'Os dados foram: {princ}')
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso cadastrado foi {maior}. Peso de ', end='')
for x in princ:
    ##pra cada elemento que o x estiver sendo, a posição 1 é o peso, e a 0 é o nome. Se o peso for igual ao maior, ele mostra o nome da pessoa x[0]
    if x[1] == maior:
        print(f'{x[0]}', end=' ')

print(f'\nO menor peso cadstrado foi {menor}. Peso de ', end='')
for y in princ:
    if y[1] == menor:
        print(f'{y[0]}', end=' ')