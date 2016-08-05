# -*- coding: utf8 -*-
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import StringProperty, ObjectProperty
from kivy.factory import Factory
from kivy.config import Config
# from datetime import datetime
import os
from os.path import abspath, dirname

Config.set('widgets', 'scroll_distance', '13')
os.environ['KIVY_DATA_DIR'] = abspath(dirname(__file__)) + '/data'

Factory.register('TouchRippleBehavior', module='uix.behaviors')
Factory.register('TabbedCarousel', module='uix.tabbedcarousel')

# from background_services import update_from_remote_schedule

'''
PyCon App:
- Displays Schedule: static √
- Static map: √
- Link to open location externally √
- Talk/Workshop details √
- Feedback ...
- Social Media:
    - Facebook
    - Twitter
- Dynamic schedule
'''


class PyConApp(App):
    '''
    Our main app class
    '''
    about_text = StringProperty('')

    # time_left = StringProperty('')

    def build(self):
        self.event_details = None
        self.about_text = '''[b]About the conference[/b]\n\nPyCon India \
is premier pan india event bringing together language experts, industry \
leaders, researchers, scientists, students & companies dealing with Python. \
\nIt is the only event of it's kind at this scale for Python in India \
attracting a diverse community of Python Developers & enthusiasts from \
all over India and aboard.\n\n\n[b]App designed and implemented by PyCon \
Team, visit us at \
[color=rgb(49,207,155)] \
[ref=http://in.pycon.org]http://pycon.org[/ref][/color][/b]
'''
        self.icon = 'data/icon.png'

    def on_pause(self):
        return True

    def on_start(self):
        # Clock.schedule_interval(self.calc_time_left, 1)
        # self.load_local_schedule()
        # update_from_remote_schedule(callback=schedule_callback)
        self._navigation_higherarchy = ['Schedule']
        from kivy.base import EventLoop
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)

    def hook_keyboard(self, window, key, *largs):
        if key == 27:
            # do what you want, return True for stopping the propagation
            self.go_back_in_history()
            return True

    def go_back_in_history(self):
        try:
            print self.root.ids.screen_manager.current
            nc = self._navigation_higherarchy.pop()
            print nc
        except IndexError:
            panel = self.root.ids.screen_schedule.ids.panel_schedule
            # curtab = panel.current_tab
            # if curtab.text == 'Audi 3':
            #     panel.current_tab = \
            #           self.root.ids.screen_schedule.ids.panel_schedule
            from kivy.utils import platform
            if platform == 'android':
                from jnius import cast
                from jnius import autoclass
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                currentActivity = cast('android.app.Activity',
                                       PythonActivity.mActivity)
                currentActivity.moveTaskToBack(True)
            self.stop()

    # def schedule_callback(self, status, data):
    #     if status == 'success':
    #         # update schedule
    #         self.load_data(data)

    # def load_local_schedule(self):
    #     import json
    #     data = json.load(open('data/pydelhi-conf-events.json'))
    #     self.load_data(data)

    # def load_data(self, data):
    #     grid = self.root.ids.grid_audi_3
    #     grid.clear_widgets()
    #     EventItem = Factory.EventItem
    #     gridadd = grid.add_widgets
    #     for hall in data.keys():
    #         talks = data[hall]
    #         for talk in talks:
    #             title = talk['schedule-item-date']
    #             date = talk['schedule-item-date']
    #             text = talk['schedule-item-text']
    #             gridadd(EventItem(title=title, time=date, spkrdetail=text))

    # def calc_time_left(self, dt):
    #     td = datetime(2016, 3, 5, 9) - datetime.now()
    #     days = td.days
    #     hours, remainder = divmod(td.seconds, 3600)
    #     minutes, seconds = divmod(remainder, 60)
    #     self.time_left = '{}d, {}:{}:{} to go'.format(days,
    #                                                   hours,
    #                                                   minutes,
    #                                                   seconds)

if __name__ == '__main__':
    app = PyConApp()
    app.run()
