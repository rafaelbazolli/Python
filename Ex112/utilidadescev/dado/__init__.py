def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.')  ##No momento que ele recebe o preço, ele já substitui as virgulas por pontos, como ele é uma string ainda
        if entrada.isalpha() or entrada.strip == '':  ##Se a entrada for alfanumérico ou se a entrada estiver vazia, com strip, retorna o erro
            print(f'\033[0;31mERRO! \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)