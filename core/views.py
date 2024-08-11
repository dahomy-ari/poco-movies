from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Banners, Side_items, Geners
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
import random

def home(request):
    banners = Banners.objects.all()
    most_popular = Movie.objects.filter(status="MP")
    trending_now = Movie.objects.filter(status="TN")
    top_rated = Movie.objects.filter(status="TR")
    side_items = Side_items.objects.all()

    context = {
        "most_popular": most_popular,
        "trending_now": trending_now,
        "banners": banners,
        "side_items": side_items,
        "top_rated": top_rated,
    }
    return render(request, "index.html", context)

def movie_detail(request, slug):
    movie = get_object_or_404(Movie, new_slug=slug)
    side_items = Side_items.objects.all()
    context = {
        "movie": movie,
        "side_items": side_items,
    }
    return render(request, "anime-details.html", context)

def suggestmovie(request):
    all_movies = list(Movie.objects.all())
    suggested_movies = random.sample(all_movies, min(len(all_movies), 3))  # Adjust the number as needed
    return render(request, 'suggestmovie.html', {'suggested_movies': suggested_movies})

def search(request):
    query = request.GET.get('q')
    if query:
        movies = Movie.objects.filter(title__icontains=query)
        context = {'movies': movies, 'query': query}
        return render(request, 'search_results.html', context)
    else:
        return render(request, 'index.html')

def anime_watching(request, slug):
    movie = get_object_or_404(Movie, new_slug=slug)
    context = {"movie": movie}
    return render(request, "anime-watching.html", context)

def blog(request):
    return render(request, "blog.html")

def categories(request, slug):
    genre = get_object_or_404(Geners, title=slug)
    movies = Movie.objects.filter(genres=genre)
    context = {
        "genre": genre,
        "movies": movies,
    }
    return render(request, "categories.html", context)

def category(request):
    movies = Movie.objects.filter(category="CO")
    context = {"movies": movies}
    return render(request, "categories.html", context)


def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email and password:
            user = authenticate(request, email=email, password=password)
            login(request, user)
            redirect("home")

    return render(request, "login.html")


def signup(request):
    if request.method == "POST":
        email = request.POST.get("email")
        name = request.POST.get("name")
        password = request.POST.get("password")
        if email and password and name:
            user = User.objects.create_user(email, password=password, username=name)
            user.save()
            redirect("home")
    return render(request, "signup.html")
