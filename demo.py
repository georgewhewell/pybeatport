from pybeatport.api import API
import urllib

api = API()

tracks = []
for page in range(1,9):
    tracks += api.do_search(term='theo', page=page)

for track in tracks:

    artist_name = track['artists'][0]['name']
    track_slug = track['slug']
    download_url = track['sampleUrl']

    print "dl: %s - %s @ %s" % (artist_name, track_slug, download_url)

    try:
        urllib.urlretrieve(download_url, '../samples/%s-%s.mp3' % (artist_name, track_slug))
    except:
        print 'err'