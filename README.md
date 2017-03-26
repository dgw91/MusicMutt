# MusicMutt

Music Mutt was developed by Nathan Arnold, Tanner Burg-Beckley, and Derrick Wilde.

It was made to be entered into eHacks2017 hackathon. Music Mutt is a responsive web app that pulls information from Spotify's REST API 
to generate a random playlist from Spotify's expansive collection, this app is perfect for someone who needs to find new music, or just 
needs a quick playlist on the go.

The back-end development of this project was produced by Tanner; it is built with Python 3.5 with the Flask library serving the pages, along with the open source spotipy library performing the api calls to the Spotify REST endpoint. The Graphic Design of this project was done by Nathan using GIMP. The front-end was developed by Derrick with HTML5 CSS3, and Javascript.

**Deployment**

This app can be deployed easily and simply to any device that has a Python 3 environment.

*Required Packages*

flask

spotipy

All required packages can be installed by pip3 package manager included in the Python 3 stack by:

pip3 install "package-name"


*Execution*

Once the repo has been cloned, execute this command in the root folder:

python3 musicmutt.py

Navigate your browser of choice to: 127.0.0.1:5000 to view the application

