from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from .models import Movies
from .serializers import MoviesSerializer


# Create your views here.

@api_view()
def home(request):
    movies = Movies.objects.all()
    serialzer = MoviesSerializer(movies, many=True)
    context = {'message': 'lets get started', 'serialzer': serialzer.data}
    return Response(context)


@api_view(['post'])
def add_movies(request):
    data = request.data
    title = data['title']
    language = data['language']
    genre = data['genre']
    rating = data['rating']
    Movies.objects.create(title=title, language=language, genre=genre, rating=rating)
    return redirect('home')
