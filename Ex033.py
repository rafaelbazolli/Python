#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = float(input('Digite um número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
# Testando qual é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Testando qual é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))
