from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.gesture import Gesture, GestureDatabase

import operator #do sortowania

from classes import *
from gesture_box import *

##======================================##
##=========	EKRANY	====================##
##======================================##

class ScreenManagement(ScreenManager): ## ZARZADZANIE EKRANAMI
	pass

class MainScreen(Screen):	## EKRAN POWITALNY
	pass
	
class AboutScreen(Screen): 	## EKRAN O APLIKACJI
	pass
	
class CategorySelectScreen(Screen):  ## EKRAN WYBORU KATEGORII
	selected = "All"
	
	
########## EKRAN SLOWNIKA ############
class DictScreen(Screen):	
	category_selected = ObjectProperty(None)

	###### GESTY ###########	
	def __init__(self, **kwargs):
		for name in gesture_strings:
			self.register_event_type('on_{}'.format(name))
		super(DictScreen, self).__init__(**kwargs)	
	
	def on_touch_down(self, touch):
		touch.ud['gesture_path'] = [(touch.x, touch.y)]
		super(DictScreen, self).on_touch_down(touch)

	def on_touch_move(self, touch):
		touch.ud['gesture_path'].append((touch.x, touch.y))
		super(DictScreen, self).on_touch_move(touch)

	def on_touch_up(self, touch):
		if 'gesture_path' in touch.ud:
			gesture = Gesture()
			gesture.add_stroke(touch.ud['gesture_path'])
			gesture.normalize()
			match = gestures.find(gesture, minscore=0.70)
			if match:
				print("{} gesture occured".format(match[1].name))
			else:
				print("No gesture recognized")
			
				
		super(DictScreen, self).on_touch_up(touch)
	
	######### HANDLERY WYDARZEN ##########
	def on_swipe_left(self):
		pass
		
	def on_swipe_right(self):
		pass
		
	def on_swipe_up(self):
		pass
		
	def on_swipe_down(self):
		pass
	
	####### ZMIANA INDEKSU Z ZAPETLENIEM ########
	
	def NextItem(self,obj,i): ##NASTEPNY ELEMENT
		if i==len(obj)-1:
			i=0
		else:
			i=i+1
		print "\nNEXT ITEM\nAktualny indeks:"+str(i)
		return i
		
	def PrevItem(self,obj,i): ##POPRZEDNI ELEMENT
		if i==0:
			i=len(obj)-1
		else:
			i=i-1
		print "\nPREVIOUS ITEM\nAktualny indeks:"+str(i)
		return i
		
	########### ZMIANA ELEMENTOW NA PODSTAWIE LISTY_OBIEKTOW(LICZBA)##############
	def ChangeLabel(self,obj,i): ## ZMIANA TEKSTU Z NAZWA
		name_text=obj[i].GetName()
		print "Aktualna nazwa:"+name_text
		print obj[i].name
		return name_text
		
	def ChangeImage(self,obj,i): ## ZMIANA SCIEZKI ZDJECIA
		imagepath = "data/img/"+str(obj[i].GetImg())
		print "Aktualny obrazek:"+imagepath
		return imagepath
		
	def ChangeCategory(self,obj,i): ## ZMIANA TEKSTU Z KATEGORIA
		categoryname_text=obj[i].GetCategory()
		print "Aktualna kategoria:"+categoryname_text
		return categoryname_text
		
	################### FILTROWANIE I SORTOWANIE ALFABETYCZNE ELEMENTOW #####################
	def CategorySelect(self,obj,cat):
		current=[]
		if cat=="ALL":
			obj.sort(key=operator.attrgetter("name"), reverse=False)
			return obj
		else:
			for item in obj:
				if item.category==cat:
					current.append(item)
			return current

	
	def on_category_selected(self, instance, value):
		self.index = 0
		category_selected = value
		self.selected_objects=self.CategorySelect(self.objects,value)
		
	
		
		
########## /EKRAN SLOWNIKA ############
		
		
	############ DANE POCZATKOWE ##############
	index=0		
	objects=[]
	current_category = "All"
	selected_objects=[]
	
	
	######################## DANE #####################
	#prosta baza danych w opraciu na liste obiektow klasy Object
	
	sport1 = Object("FOOTBALL","SPORT","football.jpg")
	sport2 = Object("BASEBALL","SPORT","baseball.jpg")
	sport3 = Object("VOLLEYBALL","SPORT","volleyball.jpg")
	sport4 = Object("TENNIS","SPORT","tennis.jpg")
	sport5 = Object("BASKETBALL","SPORT","basketball.jpg")
	sport6 = Object("BILLIARDS","SPORT","billiards.jpg")
	objects.append(sport1)
	objects.append(sport2)
	objects.append(sport3)
	objects.append(sport4)
	objects.append(sport5)
	objects.append(sport6)
	food1 = Object("BANANA","FRUITS","banana.jpg")
	food2 = Object("CHERRY","FRUITS","cherry.jpg")
	food3 = Object("LEMON","FRUITS","lemon.jpg")
	food4 = Object("PEACH","FRUITS","peach.jpg")
	food5 = Object("PEAR","FRUITS","pear.jpg")
	food6 = Object("RASPBERRY","FRUITS","raspberry.jpg")
	objects.append(food1)
	objects.append(food2)
	objects.append(food3)
	objects.append(food4)
	objects.append(food5)
	objects.append(food6)
	veg1 = Object("AVOCADO","VEGETABLES","avocado.jpg")
	veg2 = Object("BROCCOLI","VEGETABLES","broccoli.jpg")
	veg3 = Object("PUMPKIN","VEGETABLES","pumpkin.jpg")
	veg4 = Object("EGGPLANT","VEGETABLES","eggplant.jpg")
	veg5 = Object("CARROT","VEGETABLES","carrot.jpg")
	veg6 = Object("TOMATO","VEGETABLES","tomato.jpg")
	objects.append(veg1)
	objects.append(veg2)
	objects.append(veg3)
	objects.append(veg4)
	objects.append(veg5)
	objects.append(veg6)
	cloth1 = Object("BLOUSE","CLOTHES","blouse.jpg")
	cloth2 = Object("BRA","CLOTHES","bra.jpg")
	cloth3 = Object("DRESS","CLOTHES","dress.jpg")
	cloth4 = Object("SKIRT","CLOTHES","skirt.jpg")
	cloth5 = Object("SOCKS","CLOTHES","socks.jpg")
	cloth6 = Object("PANTIES","CLOTHES","panties.jpg")
	objects.append(cloth1)
	objects.append(cloth2)
	objects.append(cloth3)
	objects.append(cloth4)
	objects.append(cloth5)
	objects.append(cloth6)
	tool1 = Object("PLIERS","TOOLS","pliers.jpg")
	tool2 = Object("SHOVEL","TOOLS","shovel.jpg")
	tool3 = Object("HAMMER","TOOLS","hammer.jpg")
	tool4 = Object("AXE","TOOLS","axe.jpg")
	tool5 = Object("SCREWDRIVER","TOOLS","screwdriver.jpg")
	tool6 = Object("SCYTHE","TOOLS","scythe.jpg")
	objects.append(tool1)
	objects.append(tool2)
	objects.append(tool3)
	objects.append(tool4)
	objects.append(tool5)
	objects.append(tool6)
	color1 = Object("BURGUNDY","COLORS","burgundy.jpg")
	color2 = Object("PURPLE","COLORS","purple.jpg")
	color3 = Object("BLUE","COLORS","blue.jpg")
	color4 = Object("PINK","COLORS","pink.jpg")
	color5 = Object("GREEN","COLORS","green.jpg")
	color6 = Object("YELLOW","COLORS","yellow.jpg")
	objects.append(color1)
	objects.append(color2)
	objects.append(color3)
	objects.append(color4)
	objects.append(color5)
	objects.append(color6)

	######################## /DANE #####################

		
