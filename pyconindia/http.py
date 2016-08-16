import requests

from kivy.logger import Logger

baseurl = 'http://junctiondemo.herokuapp.com/api/v1'

def get_request(endpoint_url, **kwargs):
    url = baseurl + endpoint_url

    Logger.info('GET request: %s' % url)
    data = requests.get(url, params=kwargs)
    return data.json()

def post_request(endpoint_url, **kwargs):
    url = baseurl + endpoint_url
    Logger.info('POST request: %s' % url)
    data = requests.post(url, data=kwargs)
    return data.json()

def conference_list():
    return get_request('/conferences/')

def venue_list(id=None):
    '''
    If id is specified, it will fetch data for that venue id
    '''

    url = '/venues/'
    if id:
        url = '%s%d/' % (url, id)
    return get_request(url)

def room_list(venue_id=None):
    url = '/rooms/'
    if venue_id:
        return get_request(url, venue=str(venue_id))
    else:
        return get_request(url)

def schedule_list(conf_id=None):
    url = '/schedules/'
    if conf_id:
        return get_request(url, conference=str(conf_id))
    else:
        return get_request(url)
