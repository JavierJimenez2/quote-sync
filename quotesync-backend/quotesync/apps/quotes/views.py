from rest_framework import viewsets
from . import models
from .models import Quote
from . import serializers
from .serializers import QuoteSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import txt_file
from django.core.paginator import Paginator
from django.db.models import Q
import datetime
import urllib.parse





class AuthorViewSet(viewsets.ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = models.Quote.objects.all()
    serializer_class = serializers.QuoteSerializer

class QuoteDetailViewSet(viewsets.ModelViewSet):
    queryset = models.Quote.objects.all()
    serializer_class = serializers.QuoteDetailSerializer

class author_books(APIView):
    def get(self, request):
        authors = models.Author.objects.all()
        data = []
        for author in authors:
            id = author.id
            books = models.Book.objects.filter(author=author)
            data.append({
                "id": id,
                "author": author.name,
                "books": [book.title for book in books]
            })
        return Response(data)

class quotePost(APIView):
    def post(self, request):
        author_name = request.data.get('author')
        book_title = request.data.get('book')
        tags = request.data.get('tags')
        body = request.data.get('body')

        if not author_name or not book_title or not body:
            return Response({"error": "Author, book, and body are required fields"}, status=status.HTTP_400_BAD_REQUEST)


        try:
            gettime = datetime.datetime.now()
            created_at = gettime.strftime("%Y-%m-%d %H:%M:%S")
            author, created = models.Author.objects.get_or_create(name=author_name)
            book, created = models.Book.objects.get_or_create(title=book_title, author=author)
            quote = models.Quote.objects.create(
                title=book_title,
                body=body,
                created=created_at,
                book=book,
            )

            if tags:
                tags = tags.split(',')
                for tag_name in tags:
                    tag, created = models.Tag.objects.get_or_create(title=tag_name)
                    quote.tags.add(tag)

            quote.save()
            return Response({"message": "Quote created successfully"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def quote_delete(request, pk):
    try:
        quote = Quote.objects.get(pk=pk)
        quote.delete()
        #
        return Response({"message": "Quote deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Quote.DoesNotExist:
        return Response({"error": "Quote not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def bulk_delete(request):
    try:
        ids = request.data.get('ids')
        if not ids:
            return Response({"error": "No IDs provided"}, status=status.HTTP_400_BAD_REQUEST)

        Quote.objects.filter(id__in=ids).delete()
        return Response({"message": "Quotes deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def quote_detail(request):
    # Obtención de los parámetros de la solicitud GET
    search = request.GET.get('search', '')  # Si no se pasa, es una cadena vacía
    sort = request.GET.get('sort', 'book')  # Orden por defecto
    order = request.GET.get('order', 'asc')  # Orden ascendente por defecto
    limit = int(request.GET.get('limit', 5))  # Límite por defecto (5)
    page = int(request.GET.get('page', 1))  # Página por defecto (1)

    # Filtrar solo si hay un valor de búsqueda (si el valor es vacío, no se hace filtrado)
    if search:
        quotes = Quote.objects.filter(
            Q(book__title__icontains=search)
        )
        print(search)
    else:
        quotes = Quote.objects.all()  # Si no hay búsqueda, devuelve todas las citas

    # Ordenar solo si se ha especificado un parámetro de orden
    if order == 'desc':
        sort = f'-{sort}'
    quotes = quotes.order_by(sort)

    # Paginación
    paginator = Paginator(quotes, limit)
    try:
        current_page = paginator.page(page)
    except Exception as e:
        return Response({"error": f"Invalid page number: {e}"}, status=400)

    # Serializar los datos y devolver la respuesta
    serializer = QuoteSerializer(current_page, many=True)

    return Response({
        "data": serializer.data,
    }, status=status.HTTP_200_OK)
    # return Response({
    #     'results': serializer.data,
    #     'total': paginator.count
    # })


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        # Obtener el archivo del request
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Validar que el archivo sea de tipo texto
        if not file.name.endswith('.txt'):
            return Response({"error": "The uploaded file is not a .txt file"}, status=status.HTTP_400_BAD_REQUEST)

        # Comprobar el tipo MIME (esto también ayuda a asegurarse de que el archivo es un archivo de texto)
        if file.content_type != 'text/plain':
            return Response({"error": "The uploaded file is not of type 'text/plain'"}, status=status.HTTP_400_BAD_REQUEST)

        # Procesar el archivo
        # Aquí se puede agregar el código para procesar el archivo
        try:
            content = file.read().decode('utf-8')
            txt_file.save_quotes_from_file(content)
            print(content)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"message": "File uploaded successfully"}, status=status.HTTP_201_CREATED)


class author_detail(APIView):
    def get(self, request, pk):
        author = models.Author.objects.get(pk=pk)
        books = models.Book.objects.filter(author=author)
        quotes = models.Quote.objects.filter(book__author=author)
        # tupla = (quote.body, quote.book.title)
        complex_data = []
        for quote in quotes:
            complex_data.append({
                "quote": quote.body,
                "book": quote.book.title
            })

        data = {
            "author": author.name,
            "books": [book.title for book in books],
            "quotes": complex_data

        }
        return Response(data, status=status.HTTP_200_OK)
