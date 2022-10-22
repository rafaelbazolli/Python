#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
cores = {'limpa':'\033[m','verde':'\033[32m','azul':'\033[34m','vermelho':'\033[31m'}
texto = 'CALCULADORA DE EMPRESTIMO'
print('--='*30,'\n{}{:^80}{}\n'.format(cores['azul'], texto, cores['limpa']),'--='*30)

casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o valor do salário? R$ '))
anos = int(input('Quantos anos de financiamento? R$ '))
prestacao = casa / (anos * 12)
min = salario * 0.3
print('\nValor da casa R$ {:.2f}. \nTempo de financiamento: {} anos'.format(casa, anos))
print('Valor da prestação: {:.2f}'.format(prestacao))

if prestacao <= min:
    print('{}Emprestimo CONCEDIDO{}'.format(cores['azul'], cores['limpa']))
else:
    print('{}Emprestimo NEGADO{}'.format(cores['vermelho'], cores['limpa']))
