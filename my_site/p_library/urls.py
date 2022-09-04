from django.urls import path
from p_library import views

app_name = 'p_library'

urlpatterns = [
    path('', views.index, name="home", ),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create', ),
    path('book/create/', views.BookCreate.as_view(), name='book_create', ),
    path('reader/create/', views.ReaderCreate.as_view(), name='reader_create', ),
    path('publisher/create/', views.PublisherCreate.as_view(), name='publisher_create', ),
    path('authors/', views.AuthorsList.as_view(), name='authors', ),
    path('books/', views.BooksList.as_view(), name="books", ),
    path('readers/', views.ReadersList.as_view(), name="readers", ),
    path('publishers/', views.PublishersList.as_view(), name="publishers", ),
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name='view_author', ),
    path('book/<int:pk>/', views.BookDetail.as_view(), name='view_book', ),
    path('reader/<int:pk>/', views.ReaderDetail.as_view(), name='view_reader', ),
    path('publisher/<int:pk>/', views.PublisherDetail.as_view(), name='view_publisher', ),
    path('author/<int:pk>/edit/', views.AuthorUpdate.as_view(), name='author_edit', ),
    path('book/<int:pk>/edit/', views.BookUpdate.as_view(), name='book_edit', ),
    path('reader/<int:pk>/edit/', views.ReaderUpdate.as_view(), name='reader_edit', ),
    path('publisher/<int:pk>/edit/', views.PublisherUpdate.as_view(), name='publisher_edit', ),
    path('book_increment/', views.book_increment, name="book_increment", ),
    path('book_decrement/', views.book_decrement, name="book_decrement", ),
    # path('author/create_many/', views.author_create_many, name='author_create_many', ),
    # path('author_book/create_many/', views.books_authors_create_many, name='author_book_create_many', ),
]
