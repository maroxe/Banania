from kivy.config import Config
#Config.set('graphics', 'maxfps', '30')


from game.game import GameApp
from kivy.lang import Builder

Builder.load_file('ui/general.kv')
Builder.load_file('ui/widgets.kv')
Builder.load_file('ui/sprites.kv')
Builder.load_file('ui/game_interface.kv')


GameApp().run()
