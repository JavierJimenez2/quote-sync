from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

router.register('author', views.AuthorViewSet, 'author')
router.register('book', views.BookViewSet, 'book')
router.register('tag', views.TagViewSet, 'tag')
router.register('quote', views.QuoteViewSet, 'quote')
router.register('quote-detail', views.QuoteDetailViewSet, 'quote-detail')


urlpatterns = [
    path('upload/', views.FileUploadView.as_view(), name='file-upload'),  # Agregar la URL de carga de archivo
    path('quote-adv/', views.quote_detail, name='quote-detail'),  # Aquí registras la vista quote_detail
    path('author-books/', views.author_books.as_view(), name='author-books'),  # Aquí registras la vista author_books
    path('quotePost/', views.quotePost.as_view(), name='quotePost'),  # Aquí registras la vista quotePost
    path('quote-delete/<int:pk>/', views.quote_delete, name='quote-delete'),  # Aquí registras la vista quote_delete
    path('quote-delete/bulk-delete/', views.bulk_delete, name='bulk-delete'),  # Aquí registras la vista bulk_delete
    path('authors/<int:pk>/', views.author_detail.as_view(), name='authors'),  # Aquí registras la vista author_detail
]

urlpatterns += router.urls
