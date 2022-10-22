altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

# 1L de tinta pinta 2m² de parede
area = altura * largura
tinta = area / 2
print('A altura da parede é: {}m.\n'
      'A largura da parede é: {}m.\n'
      'A área da parede é: {:.2f}m².\n'
      'Quantidade de tinta necessária para pintar é: {:.2f} litros.'.format(altura, largura, area, tinta))
