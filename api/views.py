from django.http import HttpResponse, request, response, HttpResponseRedirect
from .forms import CreateNewList
from app.models import Playlist
from app.views import PlaylistViewSet
from django import template
from app.serializers import PlaylistSerializer
from django.shortcuts import render
import requests
import pytemperature
from spotipy.oauth2 import SpotifyClientCredentials
import random
import spotipy
from .numcheck import num_there

client_credentials_manager = SpotifyClientCredentials(client_id='YOUR_CLIENT_ID',client_secret='YOUR_CLIENT_SECRET')
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

n = random.randint(1,15)

def index(request):

    if request.method == "POST":
        form = CreateNewList(request.POST)
        if form.is_valid():          
            n = form.cleaned_data["cidade"] # Name of the city posted.

            if num_there(n) == True:
                cords = n.split(',')

                lat = cords[0]
                lon = cords[1]

                url = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=b77e07f479efe92156376a8b07640ced".format(lat, lon)
            else:
                url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=b77e07f479efe92156376a8b07640ced".format(n)

            r = requests.get(url).json()
            weather = (r["main"])
            tempkelvin = weather["temp"]
            temp = pytemperature.k2c(tempkelvin)
            temperatura = str(temp)[:2] # Get the temperature of the city written.
            
            city_name = r["name"] # Get the name of the city based on the API

            if temp > 30:
                playlistcategory = 'party'
            elif temp > 15 < 30:
                playlistcategory = 'pop'
            elif temp >= 10 < 14:
                playlistcategory = 'rock'
            else:
                playlistcategory = 'classical'
                
            results = spotify.category_playlists(category_id=playlistcategory, limit=20) # Get the playlist of determined category
            playlists = results['playlists']
            pl = playlists['items']
            playlistsongs = pl[0]['name']
            get_uri = pl[0]['uri'] # Get the id of the playlist to send to the track picker
                
            albums = spotify.playlist_tracks(get_uri, limit=50) # Get the track list of playlist
            get_items = albums['items']
            music_track = get_items[0]['track']
            music = music_track['name']

            s = Playlist.objects.all()
            s.delete()
            t = Playlist(cidade=city_name, temp=temperatura, playlist=playlistsongs, musica=music)
            t.save()
            

    else:
        form = CreateNewList()
    objs = Playlist.objects.last()
    print(objs)
    return render(request, "index.html", {"form":form, "test":objs})
