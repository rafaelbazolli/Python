preco = float(input('Digite o preço do produto: R$ '))
novo = preco - (preco * 0.05)
print('O preço do produto é R$ {:.2f}.\nO preço do produto com desconto  de 5% é R$ {:.2f}.'.format(preco, novo))
