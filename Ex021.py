import pygame
pygame.init()
# escolhendo o arquivo
pygame.mixer.music.load('Ex021.mp3')
# colocando o arquivo para tocar
pygame.mixer.music.play()
# vai aguardar até a musica acabar , para então finalizar o programa
pygame.event.wait()

