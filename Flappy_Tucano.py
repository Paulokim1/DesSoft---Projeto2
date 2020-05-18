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
TOUCAN_WIDTH = 50
TOUCAN_HEIGHT = 38
toucan_img = pygame.image.load('assets/img/meteorBrown_med1.png').convert_alpha()
toucan_img_small = pygame.transform.scale(toucan_img, (TOUCAN_WIDTH, TOUCAN_HEIGHT))

#Iniciação do jogo
GAME = True
FUNDO = pygame.image.load('Fundo.jpeg').convert()


#Loop principal
while GAME:
    # ----- Trata eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    WINDOW.fill((0, 0, 0))  # Preenche com a cor branca
    WINDOW.blit(FUNDO, (10, 10))

    pygame.display.update()

#Finalização do código
pygame.quit()