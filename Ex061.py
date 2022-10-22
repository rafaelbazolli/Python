#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('GERADOR DE P.A.','=='*20)
p = int(input('Primeiro termo: '))
razao = int(input('Razão da P.A.: '))

termo = p
i = 1
while i <=10:
    print('{} -> '.format(termo), end='')
    termo += razao
    i += 1
print('FIM')