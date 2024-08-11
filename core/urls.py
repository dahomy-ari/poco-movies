from django.urls import path
from .views import (
    home,
    movie_detail,
    anime_watching,
    blog,
    categories,
    user_login,
    signup,
    category,
    search,
    suggestmovie,
)

urlpatterns = [
    path("", home, name="home"),
    path("movie_detail/<slug:slug>", movie_detail, name="movie_detail"),
    path("anime-watching/<slug:slug>", anime_watching, name="anime-watching"),
    path("blog/", blog, name="blog"),
    path("category/", category, name="category"),
    path('categories/<slug:slug>/', categories, name='categories'),
    path("login/", user_login, name="login"),
    path('search/', search, name='search'),
    path("signup/", signup, name="signup"),
    path('suggestmovie/', suggestmovie, name='suggestmovie'),
]
