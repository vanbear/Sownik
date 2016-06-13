#======================================#
#=========	PIKI	===================#
#======================================#

from classes import *
from screens import *

#======================================#
#=========	MODULY	===================#
#======================================#

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder

#======================================#
#=========	CONFIG	===================#
#======================================#

#Config.set('graphics','height',500)
#Config.set('graphics','width',350)

#======================================#
#=========	MAIN	===================#
#======================================#

layout = Builder.load_file("main.kv")
class MainApp(App):
    def build(self):
		return layout
	

		
if __name__ == '__main__':
    MainApp().run()
