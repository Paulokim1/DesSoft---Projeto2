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

SPEED = 75

GRAVITY = 5 
#inicia sprites
class Tucano(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image = TUCANO
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH/2
		self.rect.bottom = HEIGHT/2
		self.speed = SPEED

	def pulo(self):
		self.rect.y -= SPEED

	def update(self):
		self.rect.y += GRAVITY 

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