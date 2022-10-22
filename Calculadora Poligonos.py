# Bibliotecas
import math
import os
from time import sleep

# Variaveis
color = {'limpa':"\033[m", 'azul':'\033[34m', 'amarelo':'\033[33m'}
space = ' '*35

#Definindo Funções
def limpar():
    os.system('cls')
    
def invalid():
    return print('\nPor favor, digite uma opção válida!\n')

def headtxt(texto):
    textoaux = 'CALCULADORA DE {}'.format(texto)
    return print('--' * 40, '\n                 {:^40}\n'.format(textoaux), '--' * 40)

def textos(op1):
    if op1 == 1:
        return 'QUADRADO'
    elif op1 == 2:
        return 'RETÂNGULO'
    elif op1 == 3:
        return 'TRIÂNGULO'
    elif op1 == 4:
        return 'PARALELOGRAMO'
    elif op1 == 5:
        return 'CÍRCULO'
    elif op1 == 6:
        return 'LOSANGO'
    elif op1 == 7:
        return 'PENTÁGONO'
    elif op1 == 8:
        return 'HEXÁGONO'

def areaquadrado(n1): #Na função, o valor que vai entrar, sempre precisa estar dentro dos parênteses
    area = pow(n1, 2)
    return area  #se não declarar o retorno, ele vai ser sempre null #

def perimetroquadrado(n1):
    perimetro = n1 * 4
    return perimetro

def diagonalquadrado(n1):
    diag = (n1 * math.sqrt(2)) #Diagonal de um quadrado é Lado * raiz de 2
    return diag

def arearetangulo(n1, n2):
    area = n1 * n2
    return area

def perimetroretangulo(n1, n2):
    perimetro = (n1 * 2) + (n2 * 2)
    return perimetro

def areatriretangulo(base, h):
    area = (base * h) / 2
    return area

def perimetrotriangulo(n1, n2, n3):
    perimetro = n1 + n2 + n3
    return perimetro

def areaparalel(n1, n2):
    area = n1 * n2
    return area

def perimetroparalel(n1, n2):
    perimetro = (n1 * 2) + (n2 * 2)
    return perimetro

def areacirculo(r):
    area = math.pi * pow(r, 2)
    return area

def perimetrocirculo(r):
    perimetro = 2 * math.pi * r
    return perimetro

def arealosango(n1, n2):
    area = (n1 * n2) / 2 #n1 e n2 são b e B
    return area

def perimetrolosango(n1, n2):
    perimetro = (n1 * 2) + (n2 * 2)
    return perimetro

def areapentagono(n1, apot):
    area = 5 * n1 * apot# Área é igual a 5 * o lado, * a apótema. Apótema é a reta entre o centro do pentágono até o meio de um dos lados
    return area

def perimetropentagono(n1):
    perimetro = n1 * 5
    return perimetro

def areahexagono(n1):
    area = (pow(n1, 2) * 3 * math.sqrt(3))/2 # A área é Lado ao quadrado, *3, * raiz de 3, sobre 2
    return area

def perimetrohexagono(n1):
    perimetro = n1 * 6
    return perimetro


opcao = 1
escolha = 0
texto = ''
while opcao != 0:
    limpar()
    print('=-' * 40, '\n{}CALCULADORA\n'.format(space), '=-' * 40)
    opcao = int(input('\n[ 1 ] Calcular Área / Perímetro \n[ 2 ] Calcular Volume\n[ 3 ] Avançado\n[ 0 ] Sair\n\nPor favor, selecione uma das opções acima: '))
    
    if opcao == 1: #CALCULAR ÁREA / PERÍMETRO
        limpar()
        op1 = 1
        print('--' * 40)
        print('                 CALCULADORA DE ÁREA/PERÍMETRO')
        print('--' * 40)
        while op1 != 0:
            limpar()
            op1 = int(input('\nDeseja calcular a área de qual figura?\n[ 1 ] QUADRADO\n[ 2 ] RETÂNGULO\n[ 3 ] TRIÂNGULO\n[ 4 ] PARALELOGRAMO\n[ 5 ] CÍRCULO\n[ 6 ] LOSANGO\n[ 7 ] PENTÁGONO\n[ 8 ] HEXÁGONO\n[ 0 ] Voltar ao Menu Principal\n\nDigite sua opção: '))
            if op1 == 1: #QUADRADO
                escolha = 1 #Denife escolha como 1, enquanto escolha for dif!=0, ele vai mostrar o cabeçalho, e por fim vai pedir a escolha do usuário
                while escolha != 0:
                    limpar() #limpar por padrão todas as vezes que for iniciar um menu novo
                    headtxt(textos(op1))  #Vai executar a função textos, e de acordo com a opção vai retornar o polígono correspondente, e já vai inserir o nome do polígono direto no head
                    n1 = float(input('Digite a medida do lado: '))
                    print('\nDe acordo com o valor informado, temos que o valor de cada um dos lados do quadrado é {:.2f}, o perímetro é {:.2f}, e sua área total é de {:.2f}².\nL = {:.2f}\nP = {:.2f}\nA = {:.2f}²\n'.format(n1, perimetroquadrado(n1), areaquadrado(n1), n1, perimetroquadrado(n1), areaquadrado(n1)))
                    print('\n[   ] Qualquer número para Repetir a opção\n[ 0 ] Voltar ao Menu Anterior\n')
                    escolha = int(input('\nDigite sua opção:  ')) #Escolha será a variavel que define voltar ao menu anterior ou manter no mesmo
                    if escolha == 0: #Se o usuário escolher 0, ele sai do laço while e parte novamente para o menu op1, da escolha de figura
                        print('Retornando ao Menu Anterior...')
                        sleep(1)
            elif op1 == 2: #RETÂNGULO
                escolha = 1
                while escolha != 0:
                    limpar()
                    headtxt(textos(op1))
                    n1 = float(input('Digite a medida do primeiro lado: '))
                    n2 = float(input('Digite a medida do segundo lado: '))
                    print('\nDe acordo com os valores informados, temos que o valor do primeiro lado é {:.2f}, o valor do segundo lado é {:.2f}, o perímetro é {:.2f}, e sua área total é de {:.2f}².\nb = {:.2f}\nh = {:.2f}\nP = {:.2f}\nA = {:.2f}²\n'.format(n1, n2, perimetroretangulo(n1, n2), arearetangulo(n1, n2), n1, n2, perimetroretangulo(n1, n2), arearetangulo(n1, n2)))
                    print('\n[   ] Qualquer número para Repetir a opção\n[ 0 ] Voltar ao Menu Anterior\n')
                    escolha = int(input('\nDigite sua opção:  '))
                    if escolha == 0:
                        print('Retornando ao Menu Anterior...')
                        sleep(1)
            elif op1 == 3: #TRIANGULO
                escolha = 1
                while escolha != 0:
                    limpar()
                    headtxt(textos(op1))
                    base = float(input('Digite o valor da base(b): '))
                    h = float(input('Digite a altura(h) do triângulo: '))
                    print('\nDe acordo com os valores informados, temos que a base do triângulo é {:.2f}, a altura é {:.2f}, e sua área total é de {:.2f}². Para mais opções com triângulos, acesse a opção AVANÇADO no Menu Principal.\nb = {:.2f}\nh = {:.2f}\nA = {:.2f}²\n'.format(base, h, areatriretangulo(base, h), base, h, areatriretangulo(base, h)))
                    print('\n[   ] Qualquer número para Repetir a opção\n[ 0 ] Voltar ao Menu Anterior\n')
                    escolha = int(input('\nDigite sua opção:  '))
                    if escolha == 0:
                        print('Retornando ao Menu Anterior...')
                        sleep(1)
            elif op1 == 4: #PARALELOGRAMO
                escolha = 1
                while escolha != 0:
                    limpar()
                    headtxt(textos(op1))
                    n1 = float(input('Digite o valor da base(b): '))
                    n2 = float(input('Digite a altura(h): '))
                    print('\nDe acordo com os valores informados, temos que o valor da base é {:.2f}, o valor da altura {:.2f}, o perímetro é {:.2f}, e sua área total é de {:.2f}²\n\nb = {:.2f}\nh = {:.2f}\nP = {:.2f}\nA = {:.2f}²\n'.format(n1, n2, perimetroparalel(n1, n2), areaparalel(n1, n2), n1, n2,perimetroparalel(n1, n2), areaparalel(n1, n2)))
                    print('\n[   ] Qualquer número para Repetir a opção\n[ 0 ] Voltar ao Menu Anterior\n')
                    escolha = int(input('\nDigite sua opção:  '))
                    if escolha == 0:
                        print('Retornando ao Menu Anterior...')
                        sleep(1)
            elif op1 == 5: #CÍRCULO
                escolha = 1
                while escolha != 0:
                    limpar()
                    headtxt(textos(op1))
                    r = float(input('Digite o valor do raio(r): '))
                    print('\nDe acordo com o valor informado, temos que o valor do raio é {:.2f}, sendo assim o diâmetro(D) do circulo é {:.2f}, o perímetro é {:.2f}, e sua área total é de {:.2f}²\n\nr = {:.2f}\nD = {:.2f}\nP = {:.2f}\nA = {:.2f}²\n'.format(r, r * 2, perimetrocirculo(r), areacirculo(r), r, r * 2, perimetrocirculo(r),areacirculo(r)))
                    print('\n[   ] Qualquer número para Repetir a opção\n[ 0 ] Voltar ao Menu Anterior\n')
                    escolha = int(input('\nDigite sua opção:  '))
                    if escolha == 0:
                        print('Retornando ao Menu Anterior...')
                        sleep(1)
            elif op1 == 6: #LOSANGO
                escolha = 1
                while escolha != 0:
                    limpar()
                    headtxt(textos(op1))
                    n1 = float(input('Digite o valor da primeira diagonal: ')) #D
                    n2 = float(input('Digite o valor da segunda diagonal: ')) #d
                    print('\nDe acordo com os valores informados, temos que o valor da primeira diagonal é {:.2f}, o valor da segunda diagonal é {:.2f}, o perímetro é {:.2f}, e sua área total é de {:.2f}².\n\nD = {:.2f}\nd = {:.2f}\nP = {:.2f}\nA = {:.2f}²\n'.format(n1, n2, perimetrolosango(n1, n2), arealosango(n1, n2), n1, n2, perimetrolosango(n1, n2),arealosango(n1, n2)))
                    print('\n[   ] Qualquer número para Repetir a opção\n[ 0 ] Voltar ao Menu Anterior\n')
                    escolha = int(input('\nDigite sua opção:  '))
                    if escolha == 0:
                        print('Retornando ao Menu Anterior...')
                        sleep(1)
            elif op1 == 7: #Cálculo somente para Pentágonos regulares, com os lados iguais e sabendo o valor da apótema #PENTÁGONO
                escolha = 1
                while escolha != 0:
                    limpar()
                    headtxt(textos(op1))
                    n1 = float(input('Digite o valor do lado(l): '))
                    apot = float(input('Digite o valor da apótema(a): '))
                    print('\nDe acordo com os valores informados, temos que o valor do lado da figura é {:.2f}, o valor da apótema é {:.2f}, o perímetro é {:.2f}, e sua área total é de {:.2f}².Para mais opções de cálculo de Pentágono sem apótema, ou a partir do raio, acesse a opção AVANÇADO no Menu Principal.\n\nl = {:.2f}\na = {:.2f}\nP = {:.2f}\nA = {:.2f}²\n'.format(n1, apot, perimetropentagono(n1), areapentagono(n1, apot), n1, apot, perimetropentagono(n1),areapentagono(n1, apot)))
                    print('\n[   ] Qualquer número para Repetir a opção\n[ 0 ] Voltar ao Menu Anterior\n')
                    escolha = int(input('\nDigite sua opção:  '))
                    if escolha == 0:
                        print('Retornando ao Menu Anterior...')
                        sleep(1)
            elif op1 == 8: #HEXÁGONO
                escolha = 1
                while escolha != 0:
                    limpar()
                    headtxt(textos(op1))
                    n1 = float(input('Digite o valor do lado(l): '))
                    print('\nDe acordo com o valor informado, temos que o valor do lado do Hexágono é {:.2f}, o perímetro é {:.2f}, e sua área total é de {:.2f}².\n\nL = {:.2f}\nP = {:.2f}\nA = {:.2f}²\n'.format(n1, perimetrohexagono(n1), areahexagono(n1), n1, perimetrohexagono(n1), areahexagono(n1)))
                    print('\n[   ] Qualquer número para Repetir a opção\n[ 0 ] Voltar ao Menu Anterior\n')
                    escolha = int(input('\nDigite sua opção:  '))
                    if escolha == 0:
                        print('Retornando ao Menu Anterior...')
                        sleep(1)
            elif op1 == 0:
                print('Retornando ao Menu Principal...')
                sleep(1)
            else:
                invalid()
                sleep(2)
    elif opcao == 2:   # CALCULAR VOLUME
        limpar()
        print(
            '\nPedimos desculpas pelo inconveniente, porém esta parte da calculadora ainda está em desenvolvimento.\n')
        sleep(3)
        print('Retornando ao Menu Principal...')
        sleep(2)
    elif opcao == 3:   # CALCULADORA AVANÇADA
        limpar()
        print('\nPedimos desculpas pelo inconveniente, porém esta parte da calculadora ainda está em desenvolvimento.\n')
        sleep(3)
        print('Retornando ao Menu Principal...')
        sleep(2)
    elif opcao == 0:   # SAIR
        print('Encerrando o programa...')
    else:              # ERRO
        invalid()
        sleep(2)

sleep(2)