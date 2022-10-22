#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
# mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[], []]

valor = 0
for c in range(0, 7):
    valor = int(input('Digite um valor: '))

    ##Se o valor for divisivel por 2, ele vai adicionar no elemento 0 da lista, que é a lista para números pares
    if valor % 2 == 0:
        lista[0].append(valor)
    ##Se o valor não for divisível por 2, vai adicionar na lista de ímpares, posição lista[1]
    else:
        lista[1].append(valor)
print(f'\nOs valores pares são: {sorted(lista[0])}')
print(f'\nOs valores ímpares são: {sorted(lista[1])}')