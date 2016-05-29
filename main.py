from game.game import GameApp
from kivy.lang import Builder

Builder.load_file('ui/widgets.kv')
Builder.load_file('ui/sprites.kv')

GameApp().run()
