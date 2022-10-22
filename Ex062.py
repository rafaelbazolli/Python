#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('GERADOR DE P.A.', '=='*20)
p = int(input('Primeiro termo: '))
razao = int(input('Razão da P.A.: '))

termo = p
i = 1
total = 0 #Vai receber o valor 10 inicial, mais o adicional digitado pelo usuario
m = 10  #Números a mais. Como sempre vão ser mostrados os 10 primeiros, já começa em 10
while m != 0:
    total = total + m
    while i <= total:  #Se a pessoa digitar +2, ele faz 10 inicial, +2, e enquanto o contador não bater 12, ele não para
        print('{} -> '.format(termo), end='')
        termo += razao
        i += 1
    print('PAUSA')
    m = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))