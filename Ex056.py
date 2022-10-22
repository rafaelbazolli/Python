#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
limpa = '\033[m'
amarelo = '\033[33m'
med = 0
velho = 0
nvelho = ''
i = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).upper().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]')).upper().strip()
    med = med + idade
    if idade > velho:
        velho = idade
        nvelho = nome
    if sexo == 'F':
        if idade < 20:
            i += 1
print('\nA média de idade do grupo é {:.2f}.'
      '\nO homem mais velho tem {} anos e se chama {}.'
      '\nAo todo são {} mulheres com menos de 20 anos.'.format((med/4), velho, nvelho, i))