'''
AboutScreen:
=============
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from uix.cards import CardsContainer, CardBoxLayout
from uix.buttons import SocialButton
import json


class AboutScreen(Screen):

    Builder.load_string('''
<AboutScreen>
    name: 'AboutScreen'
    BoxLayout:
        orientation: 'vertical'
        TopBar
        CardsContainer:
            size_hint_y: 1
            CardBoxLayout:
                AsyncImage
                    id: logo
                    source: 'data/images/logo.png'
                SocialButton:
                    size_hint: 1, .2
                    id: website
                    social_image: 'data/images/social/website.png'
                Label:
                    text: '2nd-3rd Nov, Workshop/Devsprints \\n 7th-8th Nov, Conference Days'
                    text_size: self.size
                    halign: 'left'
                    valign: 'center'
                    font_size: dp(24)
                    bold: True
                    color: 0, 0, 0, 1
                Label:
                    id: about
                    text: ''
                    text_size: self.size
                    halign: 'left'
                    valign: 'top'
                    font_size: dp(22)
                    color: 0, 0, 0, 1
    ''')

    def on_pre_enter(self):

        with open('eventsapp/data/jsonfiles/about.json') as data_file:
            data = json.load(data_file)

        data = data.get("0.0.1")[0]

        self.ids.logo.source = data['logo']
        self.ids.website.social_address = data['website']
        self.ids.about.text = data['about']
