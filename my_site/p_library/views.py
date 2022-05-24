from p_library.models import Author, Book, Friend, PublishingHouse, BookFriend
from p_library.forms import AuthorForm, BookForm, PublisherForm
from django.views.generic import CreateView, ListView
# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.forms import formset_factory
from django.http.response import HttpResponseRedirect


# from django.contrib.auth.decorators import permission_required


def index(request):
    # template = loader.get_template('index.html')    
    welcome_dict = {
        "welcome_phrase": "Добро пожаловать в мою библиотеку!\n"
                          "Всего в моей библиотеке книг различных авторов -   "
                          "На данный момент в библиотеку записано читателей -  ",
    }
    # return HttpResponse(template.render(welcome_dict, request,)) 
    return render(request, 'p_library/index.html', context=welcome_dict, )


# def books(request):
#     # template = loader.get_template('books.html')
#     books = Book.objects.all().select_related()
#     biblio_data = {
#         "title": "Книги",
#         "books": books,
#     }
#     # return HttpResponse(template.render(biblio_data, request,)) 
#     return render(request, 'p_library/books.html', context=biblio_data, )


# def publishers(request):
#     # template = loader.get_template('publishers.html')
#     pub_houses = PublishingHouse.objects.all().select_related()
#     # books = Book.objects.all().select_related()
#     books_counter = Book.objects.count()
#     pub_houses_data = {
#         "title": "Книжные издательства",
#         "pub_houses": pub_houses,
#         # "books": books,
#         "books_counter": books_counter,
#     }
#     # return HttpResponse(template.render(pub_houses_data, request,)) 
#     return render(request, 'p_library/publishers.html', context=pub_houses_data, )


def copy_count_change(request, action, path_='/books/'):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect(path_)
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect(path_)
            if action == '+':
                book.copy_count += 1
            elif action == '-':
                if book.copy_count < 1:
                    book.copy_count = 0
                elif book.copy_count == len(book.friends.all()):
                    ...
                else:
                    book.copy_count -= 1
            book.save()
        return redirect(path_)
    else:
        return redirect(path_)


def book_increment(request):
    return copy_count_change(request, '+')


def book_decrement(request):
    return copy_count_change(request, '-')


class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_create')
    template_name = 'p_library/author_edit.html'


class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('p_library:book_create')
    template_name = 'p_library/book_edit.html'


class PublisherCreate(CreateView):
    model = PublishingHouse
    form_class = PublisherForm
    success_url = reverse_lazy('p_library:publisher_create')
    template_name = 'p_library/publisher_edit.html'    

class AuthorsList(ListView):
    model = Author
    template_name = 'p_library/authors_list.html'
    context_object_name = 'authors'
    extra_context = {'title': 'Авторы'}


class BooksList(ListView):
    model = Book
    template_name = 'p_library/books_list.html'
    context_object_name = 'books'
    extra_context = {'title': 'Книги'}
    # friend_count = len(Book.friends)

    # def get_context_data(self, **kwargs):
    #     return super().get_context_data(**kwargs)


class PublishersList(ListView):
    model = PublishingHouse
    template_name = 'p_library/publishers_list.html'
    context_object_name = 'pub_houses'
    extra_context = {'title': 'Издательства'}


class FriendsList(ListView):
    model = Friend
    template_name = 'p_library/friends_list.html'
    context_object_name = 'friends'
    extra_context = {'title': 'Мои друзья - читатели'}


def view_author(request, auth_id):
    author = Author.objects.get(pk=auth_id)
    books = Book.objects.filter(author=auth_id)
    author_data = {
        'name': author.full_name,
        'books': books,
    }
    return render(request, 'p_library/view_author.html', context=author_data, )


def view_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    friends = BookFriend.objects.filter(book=book_id)
    book_data = {
        'title': book.title,
        'author': book.author,
        'copy': book.copy_count,
        'friends': friends,
    }
    return render(request, 'p_library/view_book.html', context=book_data, )


def view_friend(request, friend_id):
    friend = Friend.objects.get(pk=friend_id)
    books = BookFriend.objects.filter(friend=friend_id)
    friend_data = {
        'name': friend.name,
        'books': books,
    }
    return render(request, 'p_library/view_friend.html', context=friend_data, )


def view_publisher(request, publisher_id):
    publisher = PublishingHouse.objects.get(pk=publisher_id)
    books = Book.objects.filter(publishing_house=publisher_id)
    publisher_data = {
        'name': publisher.name,
        'books': books,
    }
    return render(request, 'p_library/view_publisher.html', context=publisher_data, )
   


def author_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm,
                                    extra=2)  # Первым делом, получим класс, который будет создавать наши формы. Обратите внимание на параметр `extra`, в данном случае он равен двум, это значит, что на странице с несколькими формами изначально будет появляться 2 формы создания авторов.
    if request.method == 'POST':  # Наш обработчик будет обрабатывать и GET и POST запросы. POST запрос будет содержать в себе уже заполненные данные формы
        author_formset = AuthorFormSet(request.POST, request.FILES,
                                       prefix='authors')  # Здесь мы заполняем формы формсета теми данными, которые пришли в запросе. Обратите внимание на параметр `prefix`. Мы можем иметь на странице не только несколько форм, но и разных формсетов, этот параметр позволяет их отличать в запросе.
        if author_formset.is_valid():  # Проверяем, валидны ли данные формы
            for author_form in author_formset:
                author_form.save()  # Сохраним каждую форму в формсете
            return HttpResponseRedirect(
                reverse_lazy('p_library:author_list'))  # После чего, переадресуем браузер на список всех авторов.
    else:  # Если обработчик получил GET запрос, значит в ответ нужно просто "нарисовать" формы.
        author_formset = AuthorFormSet(
            prefix='authors')  # Инициализируем формсет и ниже передаём его в контекст шаблона.
    return render(request, 'p_library/manage_authors.html', {'author_formset': author_formset})


def books_authors_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=2)
    BookFormSet = formset_factory(BookForm, extra=2)
    if request.method == 'POST':
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')
        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')
        if author_formset.is_valid() and book_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
            for book_form in book_formset:
                book_form.save()
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))
    else:
        author_formset = AuthorFormSet(prefix='authors')
        book_formset = BookFormSet(prefix='books')
    return render(
        request,
        'p_library/manage_books_authors.html',
        {
            'author_formset': author_formset,
            'book_formset': book_formset,
        }
    )
