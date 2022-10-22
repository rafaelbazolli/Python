#importando somente o módulo hipotenusa, de dentro da biblioteca math
from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = hypot(co, ca)
print('O valor da Hipotenusa é {:.2f}.'.format(h))
