# Recebe a frase eliminando os espaços no inicio/fim, e jogando todos os caracteres da string para maiúsculo
# comando .find() sempre retorna a posição
frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição: {}'.format(frase.find('A')+1))
# como eu quero a ultima aparição do A, vai começar a varredura à partir do lado direito
print('A ultima letra A apareceu na posição: {}'.format(frase.rfind('A')+1))
