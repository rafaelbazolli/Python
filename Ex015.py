#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos Km rodados? '))

valor = (dias * 60) + (km * 0.15)
print('\nO carro permaneceu alugado por {} dias. A distância percorrida foi de {:.2f}Km.\n'
      'O total a ser pago pelo aluguel é R$ {:.2f}.'.format(dias, km, valor))
