from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', context={'movies': movies})

def get(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movies/get.html', context={'movie': movie})


def post(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'movies/post.html', context={'form': form})

def delete(request, pk):
    movies = Movie.objects.all()
    Movie.objects.get(id=pk).delete()
    return render(request, 'movies/index.html', context={'movies': movies})

def put(request, pk):
    movie = Movie.objects.get(id=pk)
    form = MovieForm(instance=movie)
    if request.method == 'POST':
        form = MovieForm(data=request.POST, instance=movie)
        if form.is_valid():
            form.save()
    return render(request, 'movies/put.html', context={'form': form, 'movie': movie})

