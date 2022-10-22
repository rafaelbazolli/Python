# print(""" """) usar para colocar textos muito grandes
frase = 'Curso em Vídeo Python'
#Fatiar
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:15:2])
print(frase[::2])
#Análise
print(frase.count('o'))
print(frase.upper().count('O')) # É possivel combinar mais de um método para o mesmo objeto.
print(len(frase))
print(len(frase.strip()))
#Transformação
print(frase.replace('Python', 'Android'))
print('Curso' in frase)
print(frase.find('urso'))
print(frase.split())
print('---'*10)
dividido = frase.split()
print(dividido) # mostra a variável dividido, que é a lista, das palavras da frase
print(dividido[2]) # mostra o elemento da posição 2 da lista frase, que é a palavra Vídeo
print(dividido[2][3]) # mostra, dentro do elemento da posição 2 da lista, o terceiro elemento dentro dele, que é a letra 'e'
