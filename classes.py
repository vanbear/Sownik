#======================================#
#=========	KLASY	===================#
#======================================#
	
class Object: ## klasa obiektu (nazwa, kategoria, sciezka do zdjecia)
	def __init__(self,name,category,img):
		self.name=name
		self.category=category
		self.img=img
	def GetName(self):
		return self.name
	def GetCategory(self):
		return self.category
	def GetImg(self):
		return self.img