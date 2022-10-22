from Ex115.lib.interface import cabecalho


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') ##rt é pra ler o nome do arquivo, verificar se ele existe
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') ##write text, escreve o texto. se o arquivo não existia, ele cria o arquivo
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print('Arquivo criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Houve um ERRO ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()



def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at') ##append no arquivo, que adiciona dados ao arquivo
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
