#importando a biblioteca math
# sqrt = raiz quadrada
# ceil = arredonda o número para cima
# floor = arredonda o número para baixo
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, math.ceil(raiz)))

# se importar a biblioteca inteira de uma vez, deve manter sempre a referencia da biblioteca antes de chamar a função especifica.
# caso use from math import sqrt,ceil  não é necessário fazer referencia
#raiz = sqrt(num)