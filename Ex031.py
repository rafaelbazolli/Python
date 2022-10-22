#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
km = float(input('Qual a distância(KM) da sua viagem: '))

print('Você está prestes a iniciar uma viagem de {}Km.'.format(km))
if km <=200:
    preco = km * 0.50
    print('O valor da passagem é R$ {:.2f}.'.format(preco))
else:
    preco = km * 0.45
    print('O valor da passagem é R$ {:.2f}.'.format(preco))
