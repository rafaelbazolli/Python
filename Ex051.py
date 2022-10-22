#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
cores = {'limpa':'\033[m', 'azulclaro':'\033[36m'}

termo = int(input('Digite o termo: ')) #Inicio
razao = int(input('Digite a razão: ')) #Razão = de quanto em quanto ele vai pular o número
ultimo = termo + (10 - 1) * razao   #Regra para cálculo do ultimo termo da PA // Up.a. = termo(ultimo - 1) * razão
for c in range(termo, ultimo + razao, razao):
    print('{}{}{}'.format(x, c, cores['limpa']), end=' -> ')
print('ACABOU')