from flask import Flask
from flask import render_template
from flask import request
import random
import auth

app = Flask(__name__, static_url_path='/static')


def generateTrack(track):
    data = u"""<div class="data">
                <img src='{0}'>
                <ul>
                    <li><iframe src="https://embed.spotify.com/?uri={1}"frameborder="0" allowtransparency="true"></iframe></li>
                    <li>Artist: {2}</li>
                    <li>Album: {3}</li>
                    <li>Track: {4}</li>
                </ul>
              </div>"""
    data.format(track['imageurl'], track['uri'], track['artist'], track['album'], track['title'])
    print data
    return data


@app.route("/playlist", methods=['POST'])
def retrieveTracks():
    genre = request.form['genre']
    numTracks = int(request.form['tracks'])
    numTracks += 1
    sp = auth.generateSpotify()
    data = """<div id="container">""" + """<div id="content">"""
    for i in range(1, numTracks):
        result = sp.search(q="genre:{0}".format(genre), limit=1, type='track')
        off = result['tracks']['total']
        rand = random.randrange(1, off-1)
        result = sp.search(q="genre:{0}".format(genre), limit=1, offset=rand, type='track')
        tracks = []
        tracks.extend(result['tracks']['items'])

        for track in tracks:
            images = []
            images.extend(track['album']['images'])
            album = type<unicode>(track['album']['name'])
            artist = type<unicode>(track['artists'][0]['name'])
            title = type<unicode>(track['name'])
            uri = type<unicode>(track['uri'])
            imageurl = type<unicode>(images[1]['url'])
            thing = {'album': album, 'artist': artist, 'title': title, 'imageurl': imageurl, 'uri': uri}
            data = data + generateTrack(thing)

        data += """</div>\n</div>"""
    return render_template('playlist.html', data=data)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)