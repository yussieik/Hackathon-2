from rest_framework import serializers
from .models import (Movie,Genre,Collection)

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class Genreializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'

