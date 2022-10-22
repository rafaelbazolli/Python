import pygame
import random
import math
from pygame import mixer

#Inicializando o pygame
pygame.init()                                              #Se não iniciar o módulo pygame, não tem como acessar nenhuma função

#Criando a tela
                                                           #Não vai funcionar se não setar pelo menos os valores width(largura) e height(altura), que são largura e altura, respectivamente
screen = pygame.display.set_mode((800, 600))               #É a tela

#Plano de fundo
background = pygame.image.load('background.png')           # Carregando a imagem de fundo

#Som de fundo
mixer.music.load('background.wav')                         #Pra música, usa o music.load, pra sons vai usar o song
mixer.music.play(-1)

#Título e Ícone
pygame.display.set_caption('Space Invaders')               #Definindo o nome que vai ser exibido no display
icon = pygame.image.load('warrior-shield.png')             #Definindo o caminho do ícone que vai ser exibido no display
pygame.display.set_icon(icon)                              #Definindo o conteúdo da variável ícone para o display. Deve ser feito nessa ordem

#Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0                                          ## vai receber lá dentro do loop o valor do movimento, baseado em quanto tempo a tecla ficou pressionada

#Inimigo
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):                                     #Vai ser usado append pra inserir os valores dentro da Lista, senão não tem como alterar
    enemyImg.append(pygame.image.load('enemy.png'))                 #randint vai dar uma posição aleatória pros eixos x e y para o inimigo dar respawn em locais distintos
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(2)
    enemyY_change.append(40)

#Tiro
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480                                                # Vai iniciar na mesma altura que a ponta da nave
bulletX_change = 0
bulletY_change = 5                                           # É a velocidade em que a bala vai andar no eixo Y subindo na tela
bullet_state = 'ready'                                       #QUando ela está carregada, ainda não dá pra ver

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)                   #.ttf é a extensão dos tipos fontes. ver depois no site quais tipos de fonte tem
textX = 10                                                   # Definindo as variáveis que vão receber a posição do texto
textY = 10                                                   #O primeiro .font é o da variável, o segundo .Font, é do módulo da fonte do pygame

#Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

def game_over_text():
    over_text = over_font.render('GAME OVER', True, (0, 255, 0))
    screen.blit(over_text, (200, 250))

def show_score(x, y):                                        #Exibe o score na tela. Sempre que for exibir texto, precisa colocar o .render, ele renderiza o texto, assim como o .blit desenha uma imagem em cima de outra
    score = font.render('Score: ' + str(score_value), True, (0, 255, 0)) #True é pra mostrar o texto na tela // cor padrão rgb no final
    screen.blit(score, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def player(x, y):                                            #Vai receber o valor do playerX e playerY padrão. E a partir dele, vão recalcular pra onde vai ser o proximo passo
    screen.blit(playerImg, (x, y))
                                                             #Faz um 'desenho', que seria inserir a imagem por cima do screen... recebe dois parâmetros, a imagem e a posição.
                                                             #Como a posição já foi definida anteriormente, só basta colocar as variaveis correspondentes

def fire_bullet(x, y):
    global bullet_state                                      #Sem essa chamada, não é possivel usar a variável que está fora da função
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))                 #Ao mudar o status do tiro, ela é inserida na screen, x+16 é pra bala sair do meio da nave(a nave mede 32), e y+10 é pra bala sair de perto do bico da nave.

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((pow(enemyX - bulletX,2)) + (pow(enemyY - bulletY, 2)))     #Fórmula raiz((enemyX-bulletX)² (enemyY-bulletY)²)
    if distance < 27:
        return True
    else:
        return False

                                                             #Se você não definir um modo de pendurar o programa aberto, o windows vai encerrar logo após alguns segundos de uso. para isso, usamos o while
                                                             #Tudo o que você precisa que seja infinito dentro do game, seja um texto, um botão ou um fundo, vai dentro desse loop
running = True
while running:                                               #Enquanto running estiver com valor True, vai continuar com a janela aberta
    screen.fill((0, 0, 50))                                  # Vai preencher o screen definindo uma cor. Padrão RGB, 3 valores, de 0 até 255... quanto menor o valor, mais claro
    screen.blit(background, (0, 0))                          #Inserindo a imagem background no fundo(screen). Não pode esquecer as coordenadas. Como ele vai ser exibido desde a parte superior da tela, precisa estar na 0,0
    for event in pygame.event.get():                         #Verifica qual o evento que foi capturado dentro do programa // pode ser um clique, uma tecla, um movimento do mouse, qualquer coisa
        if event.type == pygame.QUIT:                        #Se o tipo do evento for o pygame.QUIT(o quit precisa estar maiúsculo), que é o botão de fechar, troca o valor do running  pra falso, e sai do while
            running = False
                                                             # se keystroke  for pressionado, checa se foi pra direita ou pra esquerda
        if event.type == pygame.KEYDOWN:                     ## verifica se alguma tecla foi pressionada, aí entra na estrutura
            if event.key == pygame.K_LEFT:                   # precisa ser event.key pra pegar a tecla // k_nomedatecla
                playerX_change = -3
            if event.key == pygame.K_RIGHT:                  # Se pressionar pra esquerda, retira valor do eixo x, e a nave vai pra esquerda. Se pressionar direita, acrescenta valor no eixo x, e a nave vai pra direita.
                playerX_change = 3
            if event.key == pygame.K_SPACE:                  #Se a tecla de espaço for pressionada, entra no condicional. CHama a função, e muda o status da bala pra fire
                if bullet_state == 'ready':                  #Só vai atirar se o player pressioar espaço, e se a bala estiver em ready. Se ela ainda não tiver atingido o topo e zerado o contador, não atira denovo. Se não fizer esse if, cada vez que você muda de lugar e aperta espaço, ele recalcula o x da bala, e o tiro não sai reto
                    bullet_sound = mixer.Sound('laser.wav')  #Só faz o som do tiro depois de pressionar espaço, independente do tiro pegar ou não
                    bullet_sound.play()                      #Essa linha e a de cima são o padrão pra tocar som
                    bulletX = playerX                        #x do tiro recebe o x do player, se o player sair do lugar, a bala continua na mesma direção
                    fire_bullet(playerX, bulletY)            #chama a função firebullet e recebe a posição X do player, pra que o tiro saia exatamente da nave, e vai usar o bulletY apenas pra ser incrementado logo abaixo, pra bala ir subindo
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                                                             # logo após o incremento, vai verificar se está dentro do range da tela, tanto o player como o inimigo
    playerX += playerX_change                                #Toda vez que a tecla for pressionada, vai receber um valor , e ele será adicionado ou subtraído do X, e vai direcionar a nave

    if playerX <= 0:
        playerX = 0
    elif playerX >=736:
        playerX = 736

    # Movimento do inimigo
    for i in range (num_of_enemies):
        #Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]                                   #valor vai começar subindo, e recebendo sempre o incremento que foi declarado lá no início na definição da função
        if enemyX[i] <= 0:                                              #bateu na esquerda, ou seja, atingiu 0 no eixo x, o incremento volta a ser positivo
            enemyX_change[i] = random.randint(1, 4)
            enemyY[i] += enemyY_change[i]                               #Inimigo encostou na parede, em qualquer lado, ele recebe o incremento e desce no eixo Y
        elif enemyX[i] >=736:                                           #bateu na distancia máxima que é a lateral direita no eixo x, o incremento vira negativo, e o inimigo vai pra esquerda
            enemyX_change[i] = (random.randint(1, 4))*-1
            enemyY[i] += enemyY_change[i]

        # Colisão
        collision = isCollision(enemyX[i], enemyY[i], bulletX,  bulletY)  # declara a variável colisão, chamando a função. Se a colisão retornar True, entra na condicional
        if collision:                                                     # Se a colisão acontecer, retorna a bapa pra bulletY, e ela volta a ficar carregada, permitindo um novo tiro
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = 'ready'
            score_value += 1
            print(score_value)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    #Movimento da bala
    if bulletY <= 0:                                          #quando a bala chegar no topo, reseta o y pra mesma coordenada que  a nave, e muda o status da bala pra carregada denovo
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state == 'fire':                                #Checa se o satus da bala nessa parte do loop, se tiver sido pressionado espaço, o status da bala é fire, então entra na condição
        fire_bullet(bulletX, bulletY)                         #Vai entrar na função, mostrar a bala, e em seguida vai ser decrescido do Y o valor 10, pra bala ir subindo até atingir o 0 no topo da tela
        bulletY -= bulletY_change



    player(playerX, playerY)                                  #Chama o método player definido anteriormente, logo após colorir o fundo. Ele precisa estar dentro do while pra aparecer durante o processo inteiro
    show_score(textX, textY)                                  #Vai chamar a função, e recebe as posições pré-definidas de x e y na declaração inicial
    pygame.display.update()                                   #Vai atualizar a tela o inteiro, enquanto estiver dentro do while. Se não fizer isso, não muda a cor do fundo