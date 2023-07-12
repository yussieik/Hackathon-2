from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import generics
from .forms import LoginForm, SignUpForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import  ListView, View, DetailView
from django.urls import reverse_lazy
from .serializers import (MovieSerializer, CollectionSerializer)
from .models import (Movie, Genre, Collection)
from rest_framework import response, status
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def test(request):
    return render(request, 'index.html')


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        print(form.errors.get_json_data())
        return render(request, 'signup.html', {'form': form})


class MyLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    redirect_authenticated_user = True
    next_page = 'home'


class LogoutView(LogoutView):
    next_page = reverse_lazy('login')


class CollectionListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Collection
    template_name = 'home.html'
    context_object_name = 'collection_list'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Collections"
        context['unwatched']=Collection.objects.filter(user = self.request.user.pk,is_finished=False)
        context['completed']=Collection.objects.filter(user = self.request.user.pk,is_finished=True)
        context['collection_list']=Collection.objects.filter(user = self.request.user.pk)
        context['logged_in_user']=self.request.user.pk
        context['user_name']=self.request.user.username.capitalize()
        return context

class CollectionDetailView(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    model = Collection
    template_name = 'collection.html'
    context_object_name = 'collection'


# API View 
class CollectionCreateAPIView(generics.CreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

# maybe to delete 
class CollectionListAPIView(generics.ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class CollectionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class MovieCreateAPIView(generics.CreateAPIView):
    # queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        genres = data.get("genres", [])
        fixed_genres = []
        for genre in genres:
            returned_genre, was_created = Genre.objects.get_or_create(name=genre)
            print(returned_genre.id)
            fixed_genres.append(returned_genre.id)
        print(data)
        data["genres"] = fixed_genres
        
        object_or_null = Movie.objects.filter(imdb_id=data["imdb_id"]).first()
        if object_or_null is None:
            return super().create(request, *args, **kwargs)
        else:
            object_or_null.collections.add(data["collections"][0])
            return response.Response(status=status.HTTP_201_CREATED)
    



 
class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer