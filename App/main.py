from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
import random

class GameWidget(Widget):
    score = NumericProperty(0)
    time_left = NumericProperty(30)

    def __init__(self, end_callback, **kwargs):
        super(GameWidget, self).__init__(**kwargs)
        self.end_callback = end_callback
        with self.canvas.before:
            Color(0.1, 0.1, 0.3, 1)
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_bg, pos=self.update_bg)

        self.target = Button(text='🎯', font_size=32, size_hint=(None, None), size=(100, 100),
                             background_normal='', background_color=(0.9, 0.2, 0.2, 1))
        self.target.bind(on_press=self.increase_score)
        self.add_widget(self.target)

        self.move_event = Clock.schedule_interval(self.move_target, 0.8)
        self.timer_event = Clock.schedule_interval(self.update_timer, 1.0)
        self.pop_sound = SoundLoader.load('pop.wav')

    def update_bg(self, *args):
        self.bg_rect.size = self.size
        self.bg_rect.pos = self.pos

    def move_target(self, dt):
        self.target.pos = (
            random.randint(0, int(self.width - self.target.width)),
            random.randint(0, int(self.height - self.target.height))
        )

    def increase_score(self, instance):
        self.score += 1
        if self.pop_sound:
            self.pop_sound.play()
        self.move_target(0)

    def update_timer(self, dt):
        if self.time_left > 0:
            self.time_left -= 1
        else:
            self.end_game()

    def end_game(self):
        self.move_event.cancel()
        self.timer_event.cancel()
        self.end_callback(self.score)

class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        title = Label(text='🎮 Catch the Target!', font_size=40, size_hint=(1, 0.3), color=(1, 1, 0, 1))
        start_btn = Button(text='Start Game', font_size=28, size_hint=(1, 0.2), background_color=(0.2, 0.6, 0.2, 1))
        start_btn.bind(on_press=self.start_game)
        layout.add_widget(title)
        layout.add_widget(start_btn)
        self.add_widget(layout)

    def start_game(self, instance):
        self.manager.current = 'game'

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.label = Label(text='Score: 0 | Time: 30', size_hint=(1, 0.1), font_size=24, color=(1, 1, 0, 1))
        self.layout.add_widget(self.label)
        self.game = GameWidget(end_callback=self.on_game_end)
        self.layout.add_widget(self.game)
        self.add_widget(self.layout)
        Clock.schedule_interval(self.update_info, 0.1)

    def update_info(self, dt):
        self.label.text = f"Score: {self.game.score} | Time: {self.game.time_left}"

    def on_game_end(self, final_score):
        popup = Popup(title='🎮 Game Over',
                      content=Label(text=f'Final Score: {final_score}', font_size=24),
                      size_hint=(None, None), size=(300, 200),
                      separator_color=(1, 0, 0, 1))
        popup.bind(on_dismiss=lambda x: self.manager.current = 'menu')
        popup.open()

class MyApp(App):
    def build(self):
        self.title = "Catch the Target!"
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(MainMenu(name='menu'))
        sm.add_widget(GameScreen(name='game'))
        return sm


MyApp().run()
