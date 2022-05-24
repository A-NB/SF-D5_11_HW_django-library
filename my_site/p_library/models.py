from string import Template

from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext as _


# import uuid

class Author(models.Model):
    class Meta:
        verbose_name = _("объект Автор")
        verbose_name_plural = _("Авторы")

    # id = models.UUIDField(default=uuid.uuid4, primary_key=True,
    #                       verbose_name=_("Уникальный ключ"))
    full_name = models.TextField(
        verbose_name=_("Имя автора"),
    )
    birth_year = models.SmallIntegerField(
        verbose_name=_("Год рождения"),
    )
    country = models.CharField(
        max_length=2,
        verbose_name=_("Страна"),
    )

    def get_absolute_url(self):
        return reverse_lazy('p_library:view_author', kwargs={'auth_id': self.pk})

    def __str__(self):
        return Template('$name').substitute(name=self.full_name)


class Book(models.Model):
    class Meta:
        verbose_name = _("объект Книга")
        verbose_name_plural = _("Книги")

    # id = models.UUIDField(default=uuid.uuid4, primary_key=True,
    #                       verbose_name=_("Уникальный ключ"))
    ISBN = models.CharField(
        max_length=13,
        verbose_name=_("Международный стандартный "
                       "книжный номер"),
    )
    title = models.TextField(
        verbose_name=_("Название"),
    )
    description = models.TextField(
        verbose_name=_("Аннотация"),
        blank=True,
    )
    year_release = models.SmallIntegerField(
        verbose_name=_("Год выхода в свет"),
        blank=True,
    )
    copy_count = models.SmallIntegerField(
        verbose_name=_("Число копий"),
        default=1,
        # validators=
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name=_("Цена"),
    )
    author = models.ForeignKey(
        "p_library.Author",
        on_delete=models.CASCADE,
        verbose_name=_("Автор"),
        blank=True,
        related_name="book_author",
    )
    publishing_house = models.ForeignKey(
        "p_library.PublishingHouse",
        verbose_name=_("Издательство"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="books",
    )
    year_publishing = models.SmallIntegerField(
        verbose_name=_("Год издания"),
        blank=True,
    )
    friends = models.ManyToManyField(
        "p_library.Friend",
        through='BookFriend',
        # through_fields=('book', 'friend'),
        symmetrical=False,
        verbose_name=_("Сейчас читают"),
        related_name="reading_books",
        # default=_("никто"),
        blank=True,
    )

    def get_absolute_url(self):
        return reverse_lazy('p_library:view_book', kwargs={'book_id': self.pk})

        # def clean(self):

    #     if self.copy_count<len(self.friends):
    #         raise ValidationError(_("Количество копий не может быть меньше количества книг, которые сейчас читают!"))
    #     return super().clean()           

    def __str__(self):
        return Template('$title').substitute(title=self.title)


class PublishingHouse(models.Model):
    class Meta:
        verbose_name = _("Издательство")
        verbose_name_plural = _("Издательства")

    name = models.TextField(
        verbose_name=_("Издательство"),
    )
    country = models.CharField(
        max_length=2,
        verbose_name=_("Страна"),
    )
    city = models.CharField(
        max_length=25, default="unknown",
        verbose_name=_("Город"),
    )

    def get_absolute_url(self):
        return reverse_lazy('p_library:view_publisher', kwargs={'publisher_id': self.pk})    

    def __str__(self):
        return Template('$name').substitute(name=self.name)


class Friend(models.Model):
    class Meta:
        verbose_name = _("Друг")
        verbose_name_plural = _("Друзья")

    name = models.TextField(
        verbose_name=_("Друг"),
    )
    address = models.TextField(
        verbose_name=_("Адрес"),
        default=_("Планета Земля"),
    )

    def get_absolute_url(self):
        return reverse_lazy('p_library:view_friend', kwargs={'friend_id': self.pk})

    def __str__(self):
        # return f'{self.name}'
        return Template('$name').substitute(name=self.name)


class BookFriend(models.Model):
    book = models.ForeignKey(
        Book,
        verbose_name=_("Сейчас читает:"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=_("пока ничего"),
        related_name="book_reading_friend",
    )
    friend = models.ForeignKey(
        Friend,
        verbose_name=_("Эту книгу сейчас читают:"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=_("пока никто"),
        related_name="friend_reading_book",
    )
    limit_copy = models.IntegerField(
        default=1,
    )
    borrow_date = models.DateField(
        verbose_name=_("Дата"),
        null=True,
        blank=True,
        auto_now=True,
    )

    def save(self, *args, **kwargs):
        if BookFriend.objects.filter(book_id=self.book_id).count() < self.book.copy_count:
            super(BookFriend, self).save(*args, **kwargs)  # Call the "real" save() method
        else:
            #raise ValidationError("К сожалению, все копии книги на руках. Зайдите попозже :)")
            return # Do nothing
