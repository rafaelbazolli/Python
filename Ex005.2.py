n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# : vem antes de atribuir qualquer caracteristica ao objeto.
# .xf = 'X' é a quantidade de casas decimais que você deseja exibir. 'f' é para indicar que se trata de uma flutuante
# end=' ' == é para indicar ao primeiro print que ele não acaba ali, vai juntar ao proximo print
# \n para quebrar linha
print('A soma é {}. O produto é {}. A divisão é {:.2f}.'.format(s, m, d), end=' ')
print('A divisão inteira é {}. A potência é: {}'.format(di,e))
