#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite a frase: ')).strip().upper() ##Removendo os espaços e deixando tudo em maiúsculo
palavras = frase.split() ##dividindo a frase, para eliminar os espaços
junto = ''.join(palavras) ##Juntando novamente as palavras, deiando ainda sem espaços
inverso = junto[::-1] ##inverso recebe 'junto', do inicio ao fim '::', e o -1 permite que ele seja recebido invertido, de tras pra frente
if inverso == junto:
    print(' \nOinverso de {} é {}. Temos um PALINDROMO.'.format(junto, inverso))
else:
    print('\nO inverso de {} é {}. NÃO é um PALINDROMO.'.format(junto, inverso))