n = str(input('Digite o seu nome completo: ')).strip()
# dividindo a variavel n usando um split, e gerando a lista nome. A lista começa em 1, não em 0 itens, não tem como criar lista com 0 itens com split
nome = n.split()
# pega o primeiro elemento da lista, na posição 0
print('Seu primeiro nome é {}.'.format(nome[0]))
# nome tem x elementos, sempre x>1. O comando vai pegar len.nome, ou seja, a quantidade do ultimo elemento, e tirar 1
# para ficar igual ao indice, que começa sempre em 0 // Len retorna o valor real. Precisa tirar 1, pra poder exibir dentro da lista
print('Seu ultimo nome é {}.'.format(nome[len(nome)-1]))
