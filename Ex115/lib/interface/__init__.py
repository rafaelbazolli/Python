def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaInt(msg):
    while True:
        try: #Tente fazer
            n= int(input(msg))
        except (ValueError, TypeError): ##Se der algum erro de valor, ou erro de tipo, entra na except
            print('\033[0;31mERRO: por favor , digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            break
        else:
            return n


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'\033[33m{c}\033[m - \033[34m{i}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc