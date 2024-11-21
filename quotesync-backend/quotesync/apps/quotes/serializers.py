from rest_framework import serializers
from .models import Author, Book, Tag, Quote



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'

class QuoteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'
        depth = 2


