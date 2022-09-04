from p_library.models import Author, Book, Reader, Publisher, BookReader
from p_library.forms import AuthorForm, BookForm, ReaderForm, PublisherForm
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy


def index(request):
    welcome_dict = {
        "welcome_phrase": f"<h5 class='mx-3'>Добро пожаловать в нашу библиотеку!<br>В нашей библиотеке на текущий момент:</h5><h6 class='mx-3'>представлено изданий - {Book.objects.count()}<br>записано читателей - {Reader.objects.count()}</h6><div class='mx-3'>Для навигации по разделам сайта воспользуйтесь<br>меню в верхней части страницы.<br>Желаем приятно и с пользой провести время!</div>",
    }
    return render(request, 'p_library/index.html', context=welcome_dict, )


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
                if book.copy_count == 1:
                    book.copy_count = 1
                elif book.copy_count == len(book.readers.all()):
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
    extra_context = {'info': 'автора'}
    template_name = 'p_library/form_edit.html'


class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    extra_context = {'info': 'книги'}    
    template_name = 'p_library/form_edit.html'


class ReaderCreate(CreateView):
    model = Reader
    form_class = ReaderForm
    extra_context = {'info': 'читателя'}    
    template_name = 'p_library/form_edit.html'


class PublisherCreate(CreateView):
    model = Publisher
    form_class = PublisherForm
    extra_context = {'info': 'издательства'}    
    template_name = 'p_library/form_edit.html'    


class AuthorsList(ListView):
    model = Author
    template_name = 'p_library/authors_list.html'
    context_object_name = 'authors'
    extra_context = {'title': 'Авторы'}

    def get_queryset(self):
        return Author.objects.prefetch_related('book_author', 'book_author__publisher')    


class BooksList(ListView):
    model = Book
    template_name = 'p_library/books_list.html'
    context_object_name = 'books'
    extra_context = {'title': 'Книги'}

    def get_queryset(self):
        return Book.objects.select_related('author', 'publisher').prefetch_related('book_reading_reader')


class PublishersList(ListView):
    model = Publisher
    template_name = 'p_library/publishers_list.html'
    context_object_name = 'publishers'
    extra_context = {'title': 'Издательства'}

    def get_queryset(self):
        return Publisher.objects.prefetch_related('books__author')  


class ReadersList(ListView):
    model = Reader
    template_name = 'p_library/readers_list.html'
    context_object_name = 'readers'
    extra_context = {'title': 'Читатели'}


class AuthorDetail(DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(author=context['author'])
        return context


class BookDetail(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['readers'] = BookReader.objects.filter(book=context['book'])
        return context


class ReaderDetail(DetailView):
    model = Reader

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = BookReader.objects.filter(reader=context['reader'])
        return context


class PublisherDetail(DetailView):
    model = Publisher

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(publisher=context['publisher'])
        return context


class AuthorUpdate(UpdateView):
    model = Author
    form_class = AuthorForm
    extra_context = {'info': 'автора'}    
    success_url = reverse_lazy('p_library:authors')
    template_name = 'p_library/form_edit.html'


class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    extra_context = {'info': 'книги'}    
    success_url = reverse_lazy('p_library:books')
    template_name = 'p_library/form_edit.html'
    

class ReaderUpdate(UpdateView):
    model = Reader
    form_class = ReaderForm
    extra_context = {'info': 'читателя'}    
    success_url = reverse_lazy('p_library:readers')
    template_name = 'p_library/form_edit.html'


class PublisherUpdate(UpdateView):
    model = Publisher
    form_class = PublisherForm
    extra_context = {'info': 'издательства'}    
    success_url = reverse_lazy('p_library:publishers')
    template_name = 'p_library/form_edit.html'     
