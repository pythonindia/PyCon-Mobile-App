'''
Welcome Screen
==============
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.app import App
from uix.buttons import ThemeButton
import json



class WelcomeScreen(Screen):

    Builder.load_string('''
<WelcomeScreen>
    name: 'WelcomeScreen'
    BoxLayout
        orientation: 'vertical'
        TopBar
            title: root.event_name_details()
        RelativeLayout
            Image
                source: 'data/images/navback.png'
                allow_stretch: True
                keep_ratio: False
            Image
                source: 'data/images/overlay.png'
                allow_stretch: True
                keep_ratio: False
            BoxLayout
                orientation: 'vertical'
                Label
                    text: 'Welcome to\\n'+ root.event_name_details()
                    text_size: self.size
                    valign: 'center'
                    halign: 'center'
                    font_size: dp(34)
                    color: 1, 1, 1, 1
                    bold: True
                BoxLayout
                    orientation: 'vertical'
                    spacing: dp(45)
                    padding: dp(45), dp(45)
                    ThemeButton:
                        size_hint: 1, .1
                        text: 'Workshop & DevSprints'
                        on_release: root.on_press_schedule('workshop')
                    ThemeButton:
                        size_hint: 1, .1
                        text: 'Conference Days'
                        on_release: root.on_press_schedule('conference')
    ''')

    def event_name_details(self):
    #this part of program loads event name from event.json
        with open('eventsapp/data/jsonfiles/event.json') as data_file:
            data = json.load(data_file)
        event_items = data.get("0.0.2")
        for items in event_items:
            event_name=items['name']
        return event_name

    def on_press_schedule(self, scheduletype):
        app = App.get_running_app()
        app.scheduledatatype = scheduletype
        manager = app.navigation_screen.ids.nav_manager
        app.load_screen('ScheduleScreen', manager=manager)
