##Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

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
        print(f'{matriz[i][j]:^5}', end='') ##print com 5 casas, centralizado
    ##Esse print serve somente pra quebrar a linha após as 3 repetições relacionadas às colunas
    print()