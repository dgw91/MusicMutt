from flask import Flask
from flask import render_template
from flask.json import jsonify
from flask import request
app = Flask(__name__, static_url_path='/static')

import spotipy
import json
import random
from spotipy.oauth2 import SpotifyClientCredentials

def generateTrack(track):
    html = """<div class="data">
                <img src='{0}'>
                <ul>
                    <li>Artist: {1}</li>
                    <li>Album: {2}</li>
                    <li>Track: {3}</li>
                    <li>{4}</li>
                </ul>
              </div>""".format(track['album']['images'][1]['url'],track['artists'][0]['name'],track['album']['name'],track['name'])
    return html

def generateHead(title):
    html = """ <!DOCTYPE html>
                <html>
                    <head>
                    <title>{0}</title>
                    <meta charset="UTF-8">
                    <link rel="stylesheet" href="css/style.css">
                    </head>
                    <body>
                        <h1>Playlist Generator</h1>
                        """.format(title)
    return html


def generateEnd():
    html = """<footer>
                <h2>Property of MusicMutt<sup>&reg;</sup></h2>
              </footer>
            </body>

            </html> """
    return html

@app.route("/playlist", methods=['POST'])
def retrieveTracks():
    genre=request.form['genre']
    numTracks=request.form['tracks']
    return render_template('playlist.html', genre=genre, numTracks=numTracks)

    cid = 'b774312c3dfb4b15a9dab8ef0f4a7f51'
    secret = '3bde03e4edec4d1abf81b059a9eabdbc'

    client_credentials_manager = SpotifyClientCredentials(cid,secret)

    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    trackDump = []
    html = generateHead("Country Playlist - MusicMutt")
    for i in range(1,numTracks+1):
        result = sp.search(q="genre:country",limit=1,type='track')
        off = result['tracks']['total']
        rand = random.randrange(1,off)
        result = sp.search(q="genre:country",limit=1,offset=rand,type='track')
        tracks = []
        tracks.extend(result['tracks']['items'])

        for track in tracks:
            images = []
            images.extend(track['album']['images'])
            thing = {'album': track['album']['name'], 'artist': track['artists'][0]['name'], 'title': track['name'], 'imageurl': images[1]['url']}
            html = html + generateTrack(track)
            # print track['album']['name'] + "\n" + track['artists'][0]['name'] + "\n" + track['name'] + "\n" + images[1]['url'] + "\n\n"
    
    
    html = html + generateEnd()
    return html

@app.route('/')
def home():
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)