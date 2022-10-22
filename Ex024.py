cidade = str(input('Digite o nome de uma cidade: ')).strip()
# valida nas 5 primeiras posições da string, se elas são equivalentes à palavra 'Santo'. o Retorno da equivalencia é booleano.
print(cidade[0:5].upper() == 'SANTO')
