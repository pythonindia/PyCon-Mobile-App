from uix.navigationdrawer import NavigationDrawer
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

import os
workingPath=os.getcwd()

class ConfrenceScreen(Screen):
    Builder.load_string('''

<ConfrenceScreen@BoxLayout>
    name:"ConfrenceScreen"
    Image
        source: 'data/images/background.png'
        
        allow_stretch: True
        keep_ratio: False
    ImgBut
        source: 'data/images/hamburger.png'
        width:dp(40)
        height:dp(40)
        size_hint_x: None
        size_hint_y: 1
        pos_hint:{"center_x":0.04,"center_y":0.95}
        allow_stretch: True
        on_release: app.navigationdrawer.toggle_state()
                 
        
 
    Label
        text:"PyCon 2017 Schedule "
        color:0, 0, 0, 1
<NavigationScreen>
    name: 'NavigationScreen'
    NavigationDrawer
        anim_type: 'slide_above_anim'
        on_parent: if self.parent: app.navigationdrawer = self
        BoxLayout
            orientation: 'vertical'
            Image
            Button
        ScreenManager
            id: nav_manager
            on_parent: if self.parent: app.load_screen('WelcomeScreen', manager=self)
  
    ''')

