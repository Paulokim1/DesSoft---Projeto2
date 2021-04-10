#Blibioteca do pygame importada
import pygame
import random

#Iniciação do código
pygame.init()
GAME = True
#Especificações sobre a janela e o seu Título
WIDTH = 800
HEIGHT = 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Tucano')

#Inicia assets
TUCANO_WIDTH = 100
TUCANO_HEIGHT = 100


TUCANO = pygame.image.load('tucano2.png').convert_alpha()
TUCANO = pygame.transform.scale(TUCANO, (TUCANO_WIDTH, TUCANO_HEIGHT))

FUNDO = pygame.image.load('wallpaper.jpg').convert()
FUNDO = pygame.transform.scale(FUNDO,(WIDTH,HEIGHT))

TRONCO = pygame.image.load('tronco_sem_fundo.png').convert_alpha()

pygame.mixer.music.load('music_game.ogg')
pygame.mixer.music.set_volume(0.10)
pygame.mixer.music.play(- 1)

som_pulo = pygame.mixer.Sound('sfx_wing.wav')




TRONCO_GAP = 100

SPEED = 10

GRAVITY = 1 


LFT = pygame.time.get_ticks()
#Pontuação
class Pontos:
	def __init__(self):
		self.pontos = 0 
		self.LFT = 0 
		self.SIT = 0 
	
	def acrescentaPontos(self, TFT):
		self.TSLF = TFT - self.LFT
		self.LFT = TFT

		self.SIT = self.SIT + self.TSLF
		if self.SIT > 1650:
			self.pontos = self.pontos + 1
			self.SIT = 0 
	
	def imprimePontos(self):
		FONTE_PONTUACAO = pygame.font.SysFont(None, 54)
		PLACAR = FONTE_PONTUACAO.render(str(self.pontos), True, (255,255,255))
		WINDOW.blit(PLACAR, (700,10))
		pygame.display.update()

#inicia sprites
class Tucano(pygame.sprite.Sprite):
	def __init__(self,som):
		pygame.sprite.Sprite.__init__(self)

		self.image = TUCANO
		self.mask = pygame.mask.from_surface(self.image)
		self.som = som
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH/2
		self.rect.bottom = HEIGHT/2
		self.speed = SPEED*2

	def update(self):
		self.speed += GRAVITY
		self.rect.y += self.speed


	
	def pulo(self):
		self.speed = -SPEED*1.5
		self.som.play()

		

class Tronco(pygame.sprite.Sprite):
	def __init__(self,inverted,xpos,ysize):
		pygame.sprite.Sprite.__init__(self)
		
		self.image = TRONCO
		self.mask = pygame.mask.from_surface(self.image) 
		self.rect = self.image.get_rect()
		self.rect[0] = xpos

		if inverted:
			self.image = pygame.transform.flip(self.image,False,True)
			self.mask = pygame.mask.from_surface(self.image) 
			self.rect[1] = - (self.rect[3] - ysize)
		else:
			self.rect[1] = HEIGHT - ysize

	def update(self):
		self.rect[0] -= SPEED

def random_size(xpos):
	size = random.randint(100,400)
	tronco = Tronco(False,xpos,size)
	tronco_invertido = Tronco(True,xpos,HEIGHT - size - TRONCO_GAP)
	return (tronco,tronco_invertido)

def is_off_screen(sprite):
	return sprite.rect[0] < -(sprite.rect[2])


tucano_group = pygame.sprite.Group()
tronco_group = pygame.sprite.Group()
player_tucano = Tucano(som_pulo)
tucano_group.add(player_tucano)


for i in range(2):
	troncos = random_size(WIDTH*i)
	tronco_group.add(troncos[0])
	tronco_group.add(troncos[1])


clock = pygame.time.Clock()
FPS = 45 

#Tela inicial
PRETO = (0,0,0)
TELA_INICIAL = True
TELA_ESPERA = False
TELA_MORTE = False
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
				TELA_ESPERA = True
		if event.type == pygame.QUIT:
			pygame.quit()



	WINDOW.blit(FUNDO,(0,0))
	WINDOW.blit(TITULO, (250, 100))
	WINDOW.blit(INSTRUCOES, (200, 220))
	WINDOW.blit(START, (250, 450))
	pygame.display.update()

contador = 3 
while TELA_ESPERA:
	FONTE_CONTAGEM = pygame.font.SysFont(None, 90)
	CONTAGEM = FONTE_CONTAGEM.render("{}".format(contador), True, (255,255,255))
	
	if contador < 0:
		break
	else:
		pygame.time.delay(1000)
		contador -= 1

	WINDOW.blit(FUNDO,(0,0))
	WINDOW.blit(CONTAGEM, (390, 50))
	tucano_group.draw(WINDOW)
	pygame.display.update()


pontos = Pontos()
#Loop principal
while GAME:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			GAME = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player_tucano.pulo()


	WINDOW.blit(FUNDO, (0,0))

	if is_off_screen(tronco_group.sprites()[0]):
		tronco_group.remove(tronco_group.sprites()[0])
		tronco_group.remove(tronco_group.sprites()[0])

		troncos = random_size(WIDTH*1.5)

		tronco_group.add(troncos[0])
		tronco_group.add(troncos[1])

	if player_tucano.rect.top > HEIGHT + 5:
		GAME = False
		TELA_INICIAL = False
	
	if pygame.sprite.groupcollide(tronco_group,tucano_group,False,False,pygame.sprite.collide_mask):
		tucano_group.draw(WINDOW)
		tronco_group.draw(WINDOW)
		tucano_group.update()
		tronco_group.update()
		pygame.display.update()
		break

	tucano_group.draw(WINDOW)
	tronco_group.draw(WINDOW)
	tucano_group.update()
	tronco_group.update()

	TFT = pygame.time.get_ticks()

	pontos.acrescentaPontos(TFT)
	pontos.imprimePontos()
	
	pygame.display.update()

#Tela Morte
TELA_MORTE = True
while TELA_MORTE:
	FONTE_MORTE = pygame.font.SysFont(None, 52)
	FONTE_FINAL = pygame.font.SysFont(None, 24)
	TEXTO_1 = FONTE_MORTE.render("Você morreu :(", True, (255,255,255))
	TEXTO_2 = FONTE_MORTE.render("Sua pontuação foi de {0}".format(pontos.pontos), True, (255,255,255))
	RESTART = FONTE_FINAL.render("Feche e abra o jogo para recomeçar", True,(255,255,255))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			TELA_MORTE = False
			GAME = False

	
	WINDOW.blit(FUNDO,(0,0))
	WINDOW.blit(TEXTO_1, (300, 100))
	WINDOW.blit(TEXTO_2, (200, 220))
	WINDOW.blit(RESTART, (250, 450))
	pygame.display.update()

#Finalização do código
pygame.quit()

