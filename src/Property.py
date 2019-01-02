from pygame import sprite

class Property(sprite.Sprite):

	def __init__(self, name, rents, mortgage, color, propertyImage):
		super().__init__()
		self.name = name
		self.rents = rents
		self.mortgage = mortgage
		self.color = color
		self.houses = 0
		self.hotel = 0
		self.image = propertyImage
		self.rect = self.image.get_rect()
	
	def update(self):
		pass
