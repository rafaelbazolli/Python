nome = str(input('Digite um nome: ')).strip() # strip remove os espaços excedentes no inicio e fim da frase
print('O nome digitado é: ', nome)
print('Com todas as letras maiúsculas: {}'.format(nome.upper()))
print('Com todas as letras minúsculas: {}'.format(nome.lower()))
# vai verificar a quantidade de letras no nome, e depois subtrair da quantidade de espaços vazios
print('Quantas letras tem(sem espaços): {}'.format(len(nome)-nome.count(' ')))
# vai procurar no nome, o primeiro espaço vazio. Vai retornar a posição em que encontrou o espaço em branco, que é o final da primeira palavra
print('Quantas letras tem o primeiro nome: {}'.format(nome.find(' ')))
