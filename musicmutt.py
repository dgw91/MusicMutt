from flask import Flask
from flask import render_template
from flask import request
import random
import auth

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
    # print genre
    numTracks = int(request.form['tracks'])
    numTracks += 1
    print "Numtracks: {0}".format(numTracks)
    sp = auth.generateSpotify()
    data = ""
    for i in range(1, numTracks):
        print "This is iteration {0}".format(i)
        result = sp.search(q="genre:{0}".format(genre), limit=1, type='track')
        off = result['tracks']['total']
        print off
        rand = random.randrange(1, off)
        rand = rand/2
        print rand
        result = sp.search(q="genre:{0}".format(genre), limit=1, offset=rand, type='track')
        tracks = []
        tracks.extend(result['tracks']['items'])

        for track in tracks:
            images = []
            images.extend(track['album']['images'])
            thing = {'album': unicode(track['album']['name']), 'artist': unicode(track['artists'][0]['name']), 'title': unicode(track['name']), 'imageurl': unicode(images[1]['url']), 'uri': unicode(track['uri'])}
            print thing
            data = data + generateTrack(thing)
            print "Data has been sent for the {0}th iter".format(i)

    return render_template('playlist.html', data=data)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)