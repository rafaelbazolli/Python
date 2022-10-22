from math import sin, cos, tan, radians
#angulos sempre precisam ser convertidos em radiano para usar dentro do sin, cos, tang
ang = float(input('Digite o valor do ângulo: '))

sen = sin(radians(ang))
cos = cos(radians(ang))
tang = tan(radians(ang))

print('O ângulo é {:.2f}º.\nO seno de {:.2f}º é {:.2f}.\nO cosseno de {:.2f}º é {:.2f}.\nA tangente de {:.2f}º é {:.2f}.'.format(ang, ang, sen, ang, cos, ang, tang))