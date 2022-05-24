from django.urls import path
from p_library import views

app_name = 'p_library'

urlpatterns = [
    path('', views.index, name="home", ),
    # path('index/', views.index,),    
    # path('books/', views.books, name="books", ),
    path('books/', views.BooksList.as_view(), name="books", ),    
    # path('authors/', views.view_author, name='authors', ),       
    path('authors/', views.AuthorsList.as_view(), name='authors', ),
    # path('publishers/', views.publishers, name="publishers", ), 
    path('publishers/', views.PublishersList.as_view(), name="publishers", ),
    path('friends/', views.FriendsList.as_view(), name="friends", ),    
    path('book_increment/', views.book_increment, name="book_increment", ),
    path('book_decrement/', views.book_decrement, name="book_decrement", ),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create', ),
    path('book/create/', views.BookCreate.as_view(), name='book_create', ),    
    path('publisher/create/', views.PublisherCreate.as_view(), name='publisher_create', ),      
    path('book/<int:book_id>/', views.view_book, name='view_book', ),          
    path('author/<int:auth_id>/', views.view_author, name='view_author', ),
    path('friend/<int:friend_id>/', views.view_friend, name='view_friend', ),   
    path('publisher/<int:publisher_id>/', views.view_publisher, name='view_publisher', ),     
    path('author/create_many/', views.author_create_many, name='author_create_many', ),
    path('author_book/create_many/', views.books_authors_create_many, name='author_book_create_many', ),
]
