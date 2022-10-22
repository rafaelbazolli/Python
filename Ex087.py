#Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.

somapares = maior = somacoluna = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#vai repetir 3x pra bater as linhas
for linha in range(0, 3):
    ##pra cada 1 repetição de linha, ele vai repetir 3x esse for pra ir preenchendo as colunas
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha} {coluna}]: '))

print('_'*30)
##Agora pra exibir a matriz da forma correta, fazer a varredura novamente exibindo um por um dos elementos, e realizando a quebra de linha
for i in range(0, 3):
    for j in range(0, 3):
        print(f'{matriz[i][j]:^5}', end='')
        if matriz[i][j] % 2 == 0: ##Se o número exibido na tela for par, ele já armazena e som na variavel somapar
            somapares += matriz[i][j]
        if j == 2: ##se a coluna for igual à posição 2, ou seja, o terceiro elemento de cada coluna, ele incrementa a soma
            somacoluna += matriz[i][j]
    print()
print('_'*30)
print(f'\nA soma dos pares é {somapares}.')
print(f'A soma dos valores da 3ª coluna é {somacoluna}')
for x in range(0,3):
    if x == 0: ## Se a coluna for 0, logo ele é o maior valor, considerando tudo da segunda linha, ou seja, a matriz[1]
        maior = matriz[1][x] ##Segunda linha, sempre matriz[1][x], única variante é a coluna, o x
    elif matriz[1][x] > maior:
        maior = matriz[1][x]

print(f'O maior valor da 2ª linha é {maior}.')


