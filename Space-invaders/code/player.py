import pygame 
from laser import Laser


class Player(pygame.sprite.Sprite):
	def __init__(self,pos,constraint,speed):
		super().__init__()
		self.image = pygame.image.load('../Space-invaders-kod/graphics/player.png').convert_alpha()
		self.rect = self.image.get_rect(midbottom = pos)
		self.speed = speed
		self.SpeedSefe = speed
		self.max_x_constraint = constraint
		self.ready = True
		self.laser_time = 0
		self.laser_cooldown = 600
		self.live = True

		self.lasers = pygame.sprite.Group()

	'''
		self.laser_sound = pygame.mixer.Sound('../Space-invaders-kod/audio/laser.wav')
		self.laser_sound.set_volume(0.5)
	'''
	def get_input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT]:
			self.rect.x += self.speed
		elif keys[pygame.K_LEFT]:
			self.rect.x -= self.speed

		if keys[pygame.K_SPACE] and self.ready:
			self.shoot_laser()
			self.ready = False
			self.laser_time = pygame.time.get_ticks()
			#self.laser_sound.play()

	def recharge(self):
		if self.live is not False:
			if not self.ready:
				current_time = pygame.time.get_ticks()
				if current_time - self.laser_time >= self.laser_cooldown:
					self.ready = True

	def constraint(self):
		if self.rect.left <= 0:
			self.rect.left = 0
		if self.rect.right >= self.max_x_constraint:
			self.rect.right = self.max_x_constraint

	def shoot_laser(self):
		self.lasers.add(Laser(self.rect.center,-8,self.rect.bottom))

	def update(self,lives,isESC):
		self.get_input()
		self.constraint()
		self.recharge()
		self.lasers.update(isESC)
		self.dead(lives)
		if lives <= 0:
			pass
		else:
			if isESC == True:
				self.pause(isESC)
			if isESC == False:
				self.Unpause(isESC)

	def pause(self, isESC):
		if isESC == True:
			self.speed = 0
	def Unpause(self, isESC):
		if isESC == False:
			self.speed = self.SpeedSefe
	def dead(self,lives):
		if lives <= 0:
			self.speed = 0
			self.live = False
			self.image = pygame.image.load('../Space-invaders-kod/graphics/deadplayer.png').convert_alpha()
