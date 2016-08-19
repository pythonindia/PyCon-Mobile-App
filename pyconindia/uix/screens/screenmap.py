from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.garden.mapview import MapView , MapMarker
from kivy.factory import Factory

class ScreenMap(Screen):

    mv = None
    Builder.load_string('''
<ScreenMap>
    name:'ScreenMap'
    MapView:
        id: map_view
        zoom: 5
''')
    
    def on_enter(self):
        
        self.ids.map_view.center_on(22.00, 77.00)   
        import json
        data = ''
        with open('data/maps.json') as fl:
            data = json.load(fl)
        locations = data
        self.locations = locations
        location_list =  locations['locations']
        for location in location_list:
            state = location.keys()[0]
            marker = MapMarker(lat = float(location[state]['lat']), lon =float(location[state]['lon'] ))
            self.ids.map_view.add_marker(marker) 
            print('Coordinates for {} are longitude: {} latitude:{}'.format(state,location[state]['lon'],location[state]['lat']))
