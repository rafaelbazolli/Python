num = int(input('Digite um número entre 0 e 9999: '))
# o numero dividido por 1 dá ele mesmo. O resto da divisão por 10 vai sobrar somente a unidade
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}...'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
