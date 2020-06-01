#Blibioteca do pygame importada
import pygame

#Iniciação do código
pygame.init()

#Especificações sobre a janela e o seu Título
WIDTH = 800
HEIGHT = 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Tucano')

#Inicia assets
TUCANO_WIDTH = 100
TUCANO_HEIGHT = 100
# TRONCO_WIDTH =
# TRONCO_HEIGHT =

TUCANO = pygame.image.load('tucano2.png').convert_alpha()
TUCANO = pygame.transform.scale(TUCANO, (TUCANO_WIDTH, TUCANO_HEIGHT))

FUNDO = pygame.image.load('wallpaper.jpg').convert()
FUNDO = pygame.transform.scale(FUNDO,(WIDTH,HEIGHT))

# TRONCO = pygame.image.load('tronco.jpg').convert_alpha()
# TRONCO = pygame.transform.scale(TRONCO,(TRONCO_WIDTH,TRONCO_HEIGHT))

SPEED = 10

GRAVITY = 1 
#inicia sprites
class Tucano(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image = TUCANO
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH/2
		self.rect.bottom = HEIGHT/2
		self.speed = SPEED*2

	def update(self):
		self.speed += GRAVITY
		self.rect.y += self.speed

	def pulo(self):
		self.speed = -SPEED*1.5
# class Tronco(pygame.sprite.Sprite):
# 	def __init__(self):
# 		pygame.sprite.Sprite.__init__(self)

# 	self.image = TRONCO 
# 	self.rect = self.image.get_rect()


sprite_group = pygame.sprite.Group()
player_tucano = Tucano()
sprite_group.add(player_tucano)

clock = pygame.time.Clock()
FPS = 30

#Tela inicial
PRETO = (0,0,0)
TELA_INICIAL = True
while TELA_INICIAL:
	FONTE_TITULO = pygame.font.SysFont(None, 48)
	FONTE_INSTRUCOES = pygame.font.SysFont(None, 24)
	TITULO = FONTE_TITULO.render("FLAPPY TUCANO", True, (255,255,255))
	INSTRUCOES = FONTE_INSTRUCOES.render("Aperte espaço para controlar a altura do tucano", True,(255,255,255))
	START = FONTE_INSTRUCOES.render("Aperte enter para começar o jogo", True, (255,255,255))
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				TELA_INICIAL = False
	WINDOW.blit(FUNDO,(0,0))
	WINDOW.blit(TITULO, (250, 100))
	WINDOW.blit(INSTRUCOES, (200, 220))
	WINDOW.blit(START, (250, 450))
	pygame.display.update()

#Loop principal
GAME = True
while GAME:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			GAME = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player_tucano.pulo()


	WINDOW.blit(FUNDO, (0,0))
	
	sprite_group.draw(WINDOW)
	sprite_group.update()

	pygame.display.update()

#Finalização do código
pygame.quit()

