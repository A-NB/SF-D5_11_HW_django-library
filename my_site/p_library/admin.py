from django.contrib import admin
from p_library.models import Author, Book, Publisher, Reader, BookReader


# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     # @staticmethod
#     # def author_full_name(obj):
#     #     return obj.author.full_name#.verbose_name

#     def who_read(self, obj):
#         return '\n'.join([f.name for f in obj.readers.all()])

#     filter_horizontal = ('readers',)
#     list_display = ('title', 'author', 'price', 'copy_count', 'who_read',) # 'author_full_name', 'price', 'copy_count',)
#     fields = ('ISBN', 'title', 'author', 'description', 'year_release', 'price', 'copy_count', 'year_publishing', 'publishing_house',)# 'readers',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_year', 'country',)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city',)


# @admin.register(Reader)
# class ReaderAdmin(admin.ModelAdmin):

#     def show_reading_books(self, obj):
#         return '\n'.join([b.title for b in obj.reading_books.all()])

#     list_display = ('name', 'address', 'show_reading_books', 'when',)
#     # filter_horizontal = ('readers',)
#     fields = ('name', 'address', 'when',)# 'reader_reading_book',)# 'reading_books',)

class BookReaderInline(admin.TabularInline):
    model = BookReader
    extra = 0
    verbose_name = ""  # "Движение книг"
    verbose_name_plural = ""  # "Движение книг"
    # list_display = ('book', 'reader', 'borrow_date',)
    # fields = ('book', 'reader', 'limit_copy',)# 'borrow_date',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = (BookReaderInline, )

@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    inlines = (BookReaderInline, )

# admin.site.register(Book, BookAdmin) 


# admin.site.register(Reader, ReaderAdmin)

# @admin.register(BookReader)
# class BookReader(admin.ModelAdmin):
#     ...


# list_display = ('name', 'country', 'city',)


# [admin.site.register(item) for item in ((Author, AuthorAdmin), (Book, BookAdmin), (Publisher, PublisherAdmin), )]
