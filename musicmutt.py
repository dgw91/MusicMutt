# coding: utf-8
from flask import Flask
from flask import render_template
from flask import request
import random
import auth


app = Flask(__name__, static_url_path='/static')


def generateTrack(track):
    data = """<div class="data">
                <img src=""" + track['imageurl'] + """>
                <ul>
                    <li><iframe src="https://embed.spotify.com/?uri=""" + track['uri'] + """" frameborder="0" allowtransparency="true"></iframe></li>
                    <li>Artist: """ + track['artist'] + """</li>
                    <li>Album: """ + track['album'] + """</li>
                    <li>Track: """ + track['title']+ """</li>
                </ul>
              </div>"""
    data.format(track['imageurl'], track['uri'], track['artist'], track['album'], track['title'])
    print (data)
    return data

def utfFix(string):
    # string = string.encode('ascii')
    return string


@app.route("/playlist", methods=['POST'])
def retrieveTracks():
    genre = request.form['genre']
    # print genre
    numTracks = int(request.form['tracks'])
    numTracks += 1
    sp = auth.generateSpotify()
    data = ""
    for i in range(1, numTracks):
        result = sp.search(q="genre:{0}".format(genre), limit=1, type='track')
        off = result['tracks']['total']
        rand = random.randrange(1, off)
        rand = int(rand/2)
        result = sp.search(q="genre:{0}".format(genre), limit=1, offset=rand, type='track')
        tracks = []
        tracks.extend(result['tracks']['items'])

        for track in tracks:
            images = []
            images.extend(track['album']['images'])
            thing = {'album': utfFix(track['album']['name']), 
                     'artist': utfFix(track['artists'][0]['name']), 
                     'title': utfFix(track['name']), 
                     'imageurl': utfFix(images[1]['url']), 
                     'uri': utfFix(track['uri'])}
            data = data + generateTrack(thing)

    return render_template('playlist.html', data=data)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)