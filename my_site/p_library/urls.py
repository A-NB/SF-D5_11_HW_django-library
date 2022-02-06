from django.urls import path
from p_library import views

app_name = 'p_library'

urlpatterns = [
    path('', views.index, name="home", ),
    # path('index/', views.index,),    
    path('books/', views.books, name="books", ),
    path('publishers/', views.publishers, name="publishers", ),
    path('book_increment/', views.book_increment, name="book_increment", ),
    path('book_decrement/', views.book_decrement, name="book_decrement", ),
    path('author/create/', views.AuthorEdit.as_view(), name='author_create', ),
    path('authors/', views.AuthorList.as_view(), name='authors', ),
    path('author/create_many/', views.author_create_many, name='author_create_many', ),
    path('author_book/create_many/', views.books_authors_create_many, name='author_book_create_many', ),
]
