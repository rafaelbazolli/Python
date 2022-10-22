nome = input('Qual o seu nome? ')
# {} vazio não tem nenhum incremento
print('Prazer em te conhecer {}!'.format(nome))
# {:10} o numero define o tamanho do espaço no qual o nome será exibido
print('Prazer em te conhecer {:10}!'.format(nome))
# {:<10} alinha o texto para a esquerda
print('Prazer em te conhecer {:<10}'.format(nome))
# {:>10} alinha o texto para a direita
print('Prazer em te conhecer {:>10} '.format(nome))
# ^ alinha o texto como centralizado
print('Prazer em te conhecer {:^10}'.format(nome))
# =^ alinha o texto como centralizado, e coloca = em volta do nome.  O = pode ser substituido por outros caracteres.
print('Prazer em te conhecer {:=^10}'.format(nome))

