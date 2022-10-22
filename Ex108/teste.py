import moeda

##Tudo que for receber a formatação da função moeda.moeda() precisa estar dentro dela, mesmo que seja o retorno de uma outra função
preco = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}.')
print(f'O dobro de R$ {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}.')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(preco, 10))}')
print(f'Diminuindo 10%, temos {moeda.moeda(moeda.diminuir(preco, 10))}')

