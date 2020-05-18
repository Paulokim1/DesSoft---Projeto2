#Blibioteca do pygame importada
import pygame

#Iniciação do código
pygame.init()

#Especificações sobre a janela e o seu Título
WIDTH = 1000
HEIGHT = 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Tucano')

#Inicia assets
TUCANO_WIDTH = 50
TUCANO_HEIGHT = 38
TUCANO = pygame.image.load('tucano.png').convert_alpha()
TUCANO_PEQUENO = pygame.transform.scale(TUCANO, (TUCANO_WIDTH, TUCANO_HEIGHT))

#Iniciação do jogo
GAME = True
FUNDO = pygame.image.load('Fundo.jpeg').convert()


#Loop principal
while GAME:
    #Trata eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME = False

    WINDOW.fill((0, 0, 0))  # Preenche com a cor branca
    WINDOW.blit(FUNDO, (10, 10))

    pygame.display.update()

#Finalização do código
pygame.quit()