#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

exp = str(input('Digite a expressão: '))

lista = []

##O for vai varrer a expressão digitada
for s in exp:
    ##Se o ítem analisado nessa repetição for um (, ele vai adicionar um ( aberto na lista.
    if s == '(':
        lista.append('(')
    ##Se o ítem for um ), ele vai entrar na condicional. Se o tamanho da lista for maior que 0, indica que já tem um ( aberto nela. Então ele dá um pop e remove um (, tornando equivalente como se um ) tivesse anulado o outro (.
    elif s == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            ## Se o tamanho da lista for 0, ele adiciona um ) a mais, e sai do laço.
            lista.append(')')
            break

##Se a lista está vazia, então a quantidade de ( digitados foi equivalente à quantidade de ) digitados
if len(lista) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')
