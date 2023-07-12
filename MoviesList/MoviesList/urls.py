"""
URL configuration for MoviesList project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import (SignUpView, MyLoginView, LogoutView,
                       CollectionListView, test, CollectionCreateAPIView,
                       MovieCreateAPIView, CollectionListAPIView, MovieListAPIView,
                       CollectionDetailView, MovieDetailAPIView, CollectionDetailAPIView)
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('test/', test, name='test'),
    path('home/', CollectionListView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/collections/create/', CollectionCreateAPIView.as_view(),
         name='collection-create'),
    path('api/collections/list', CollectionListAPIView.as_view(),
         name='collection-list'),
    path('api/collections/<int:pk>', CollectionDetailAPIView.as_view(),
         name='collection-detail'),
    path('api/movies/create/', MovieCreateAPIView.as_view(),
         name='movie-create'),
    path('api/movies/list/', MovieListAPIView.as_view(),
         name='movie-list'),
     path('api/movies/<int:pk>', MovieDetailAPIView.as_view(),
         name='movie-detail'),
    path('collections/<int:pk>', CollectionDetailView.as_view(),
         name='collection'),
]
