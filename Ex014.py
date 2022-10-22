#Conversor de temperatura
temp = float(input('Informe a temperatura em ºC: '))
f = (temp * 9) / 5 + 32
print('A temperatura {:.2f}ºC corresponde à {:.2f}ºF!'.format(temp, f))
