#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

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


def leiaFloat(msg):
    while True:
        try: #Tente fazer
            n= float(input(msg))
        except (ValueError, TypeError): ##Se der algum erro de valor, ou erro de tipo, entra na except
            print('\033[0;31mERRO: por favor , digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            break
        else:
            return n


num = leiaInt('Digite um número inteiro: ')
print(f'O valor digitado foi {num}')
f = leiaFloat('Digite um número real: ')
print(f'O valor digitado foi {f}')
