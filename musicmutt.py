from flask import Flask
from flask import render_template
from flask import request
from HTMLParser import HTMLParser

import spotipy
import random
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__, static_url_path='/static')
def generateTrack(track):
    data = """<div class="data">
                <img src='{0}'>
                <ul>
                    <li><iframe src="https://embed.spotify.com/?uri={1}"frameborder="0" allowtransparency="true"></iframe></li>
                    <li>Artist: {2}</li>
                    <li>Album: {3}</li>
                    <li>Track: {4}</li>
                </ul>
              </div>""".format(track['imageurl'], track['uri'], track['artist'], track['album'], track['title'])
    print data
    return data


@app.route("/playlist", methods=['POST'])
def retrieveTracks():
    genre = request.form['genre']
    print genre
    numTracks = int(request.form['tracks'])
    
    numTracks += 1
    print numTracks
    cid = 'b774312c3dfb4b15a9dab8ef0f4a7f51'
    secret = '3bde03e4edec4d1abf81b059a9eabdbc'

    client_credentials_manager = SpotifyClientCredentials(cid,secret)

    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    trackDump = []
    data = ""
    for i in range(1, numTracks):
        result = sp.search(q="genre:{0}".format(genre), limit=1, type='track')
        off = result['tracks']['total']
        rand = random.randrange(1, off)
        result = sp.search(q="genre:{0}".format(genre),limit=1,offset=rand,type='track')
        tracks = []
        tracks.extend(result['tracks']['items'])

        for track in tracks:
            images = []
            images.extend(track['album']['images'])
            thing = {'album': track['album']['name'], 'artist': track['artists'][0]['name'], 'title': track['name'], 'imageurl': images[1]['url'], 'uri': track['uri']}
            data = data + generateTrack(thing)
        print i

    return render_template('playlist.html', data=data)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)