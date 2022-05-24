from django.contrib import admin
from p_library.models import Author, Book, PublishingHouse, Friend, BookFriend


# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     # @staticmethod
#     # def author_full_name(obj):
#     #     return obj.author.full_name#.verbose_name

#     def who_read(self, obj):
#         return '\n'.join([f.name for f in obj.friends.all()])

#     filter_horizontal = ('friends',)
#     list_display = ('title', 'author', 'price', 'copy_count', 'who_read',) # 'author_full_name', 'price', 'copy_count',)
#     fields = ('ISBN', 'title', 'author', 'description', 'year_release', 'price', 'copy_count', 'year_publishing', 'publishing_house',)# 'friends',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_year', 'country',)


@admin.register(PublishingHouse)
class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city',)


# @admin.register(Friend)
# class FriendAdmin(admin.ModelAdmin):

#     def show_reading_books(self, obj):
#         return '\n'.join([b.title for b in obj.reading_books.all()])

#     list_display = ('name', 'address', 'show_reading_books', 'when',)
#     # filter_horizontal = ('friends',)
#     fields = ('name', 'address', 'when',)# 'friend_reading_book',)# 'reading_books',)

class BookFriendInline(admin.TabularInline):
    model = BookFriend
    extra = 0
    verbose_name = ""  # "Движение книг"
    verbose_name_plural = ""  # "Движение книг"
    # list_display = ('book', 'friend', 'borrow_date',)
    # fields = ('book', 'friend', 'limit_copy',)# 'borrow_date',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = (BookFriendInline, )


class FriendAdmin(admin.ModelAdmin):
    inlines = (BookFriendInline, )

# admin.site.register(Book, BookAdmin) 


admin.site.register(Friend, FriendAdmin)

# @admin.register(BookFriend)
# class BookFriend(admin.ModelAdmin):
#     ...


# list_display = ('name', 'country', 'city',)


# [admin.site.register(item) for item in (Author, Book, PublishingHouse,)]
