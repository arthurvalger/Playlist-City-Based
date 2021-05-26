from django.shortcuts import render
from rest_framework import viewsets
from .models import Playlist
from .serializers import PlaylistSerializer

# Create your views here.

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer