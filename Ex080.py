#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
for i in range(0, 5):
    #Recebendo o valor
    num = int(input('Digite um valor: '))

    ##Se for a primeira repetição, ou se o número for maior que o último, ele só faz o append, que vai salvar o número no final da lista, mantendo a ordem crescente
    if i == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado na posição final da lista...')
    else:
        pos = 0
        ##Se o número não for maior que o último, agora é necessário ver em qual posição ele se encaixaria
        while pos < len(lista):
            ##Se o número digitado for menor ou igual à lista na pos indicada, ele sobrepoe a posição.
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista...')
                break
                ##Depois de adicionado, quebra o laço e vola ao for inicial para continuar pedindo valores
            ##Incremento que vai varrer a lista, na pos 0, 1, 2.... e ir comparando num com lista[pos]
            pos +=1

print(f'\nOs valores digitados, em ordem, são: {lista}')
