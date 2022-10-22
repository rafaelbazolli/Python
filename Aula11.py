# \033[m cancela a cor, senão ela vai até o fim da linha
print('\033[7;37;40mOlá Mundo!')
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m.'.format(a, b))