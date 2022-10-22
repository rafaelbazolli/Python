nome = str(input('Digite seu nome completo: ')).strip()
# se for procurar por algo especifico, em algum lugar desconhecido do texto, usa o " " in .
# converter tudo pra maiusculo para eliminar problemas com digitação
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))