import urllib
import urllib2
import json

class API(object):

    API_ROOT = 'http://api.beatport.com/'

    def do_api_call(self, *args, **kwargs):

        url = self.API_ROOT + '/'.join(args) + '?' + urllib.urlencode(kwargs)
        print "opening %s" % url
        response = urllib.urlopen(url).read()
        data = json.loads(response)
        return data

    def do_search(self, **kwargs):
        result = self.do_api_call('catalog', '3', 'tracks', perPage=50, **kwargs)
        return result['results']
        