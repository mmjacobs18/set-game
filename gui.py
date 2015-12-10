from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

class RootWidget(GridLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RootWidget, self).__init__(**kwargs)

        # let's add a Widget to this layout
        self.add_widget(
            Image(source='cards/1_green_diamond_clear.JPG'))
           # Button(
            #    text="Hello World",
            #    size_hint=(.5, .5),
             #   pos_hint={'center_x': .5, 'center_y': .5}))


class MainApp(App):

    def on_touch_down(self,touch):
        if after:
            print "Fired after the event has been dispatchedi!"
        else:
            Clock.schedule_once(lambda dt: self.on_touch_down(touch, True))
            return super(MyLabel, self).on_touch_down(touch)

    def build(self):
        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)

        with root.canvas.before:
            Color(0, 1, 0, 1)  # green; colors range from 0-1 not 0-255
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == '__main__':
    MainApp().run()
#Using the kv Language:

from kivy.app import App
from kivy.lang import Builder


root = Builder.load_string('''
FloatLayout:
    canvas.before:
        Color:
            rgba: 0, 1, 0, 1
        Rectangle:
            # self here refers to the widget i.e FloatLayout
            pos: self.pos
            size: self.size
    Button:
        text: 'Hello World!!'
        size_hint: .5, .5
        pos_hint: {'center_x':.5, 'center_y': .5}
''')

class MainApp(App):

    def build(self):
        return root

if __name__ == '__main__':
    MainApp().run()
