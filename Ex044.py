#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto / – à vista no cartão: 5% de desconto / – em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros
cores = {'limpa':'\033[m', 'verde':'\033[32m', 'azulclaro':'\033[36m', 'roxo':'\033[35m', 'vermelho':'\033[31m'}
texto = 'LOJAS GUANABARA'
print('==='*30, '\n{}{:^90}{}\n'.format(cores['roxo'], texto, cores['limpa']), '==='*30)

preco = float(input('Preço das compras: R$ '))
print("""\nEscolha a forma de pagamento:
[ 1 ] à vista dinheiro / cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
opcao = int(input('Qual a opção? '))
if opcao == 1:
    valor = preco - (preco * 0.1)
    metodo = 'Você escolheu a opção 1, pagamento à vista dinheiro/cheque.'
elif opcao == 2:
    valor = preco - (preco * 0.05)
    metodo = 'Você escolheu a opção 2, pagamento à vista no cartão.'
elif opcao == 3:
    valor = preco
    metodo = 'Você escolheu a opção 3, pagamento em 2x no cartão.\nValor de cada parcela: R$ {:.2f}'.format(valor/2)
elif opcao == 4:
    nparc = int(input('O valor será dividido em quantas parcelas? '))
    valor = preco + (preco * 0.2)
    parcela = valor / nparc
    metodo = 'Você escolheu a opção 4, pagamento em {}x no cartão.\nValor de cada parcela: R$ {:.2f}'.format(nparc, parcela)
else:
    valor = preco
    metodo = 0
    print('\nOPÇÃO INVÁLIDA DE PAGAMENTO! TENTE NOVAMENTE.'.format(cores['vermelho']))

if metodo != 0:
    print('\nValor da compra: R$ {:.2f}\n{}\nValor final: R$ {:.2f}'.format(preco, metodo, valor))