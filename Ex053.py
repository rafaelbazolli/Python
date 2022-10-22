#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite a frase: ')).strip().upper() ##Removendo os espaços e deixando tudo em maiúsculo
palavras = frase.split() ##dividindo a frase, para eliminar os espaços
junto = ''.join(palavras) ##Juntando novamente as palavras, deiando ainda sem espaços
inverso = ''
for letra in range(len(junto)-1, -1, -1): ##Inicio do laço deve ser igual ao tamanho da frase -1 sem espaços, que é a ultima letra
    inverso += junto[letra]               ##A varredura é feita de tras pra frente, então ela vai até -1 ou até 0, andando na razão -1
if inverso == junto:
    print(' \nOinverso de {} é {}. Temos um PALINDROMO.'.format(junto, inverso))
else:
    print('\nO inverso de {} é {}. Não é um PALINDROMO.'.format(junto, inverso))