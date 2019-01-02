from pygame import sprite

class Piece(sprite.Sprite):

	def __init__(self, pieceImage):
		super().__init__()
		self.image = pieceImage
		self.rect = self.image.get_rect()
		self.spotNumber = 0
		self.properties = {}
	
	def update(self, diceRoll):
		pass
	
	def addProperty(self, monopolyProperty):
		pass
	
	def deleteProperty(self, monopolyProperty):
		pass
