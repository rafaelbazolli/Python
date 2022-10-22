def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>4.2f}'.replace('.',',')


def resumo(preco=0, taxaa=10, taxad=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(32))
    print('-' * 30)
    print(f'Preço analisado:\t{moeda(preco)}')
    print(f'Dobro do preço:\t\t{dobro(preco, True)}') ##como já está dentro do módulo não tem o moeda.dobro()
    print(f'Metade do preço:\t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxad}% de redução: \t\t{diminuir(preco, taxad, True)}')
    print('-' * 30)
