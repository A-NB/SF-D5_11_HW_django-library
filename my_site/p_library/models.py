from string import Template
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


class Author(models.Model):
    class Meta:
        verbose_name = _("объект Автор")
        verbose_name_plural = _("Авторы")

    full_name = models.TextField(
        verbose_name=_("Имя автора"),
        default=_("Неизвестен"),
    )
    birth_year = models.PositiveSmallIntegerField(
        verbose_name=_("Год рождения"),
        blank=True,
        null=True,
    )
    country = models.CharField(
        verbose_name=_("Страна"),
        max_length=2,        
        blank=True,
        null=True,        
    )

    def get_absolute_url(self):
        return reverse_lazy('p_library:view_author', kwargs={'pk': self.pk})

    def __str__(self):
        return Template('$name').substitute(name=self.full_name)


class Book(models.Model):
    class Meta:
        verbose_name = _("объект Книга")
        verbose_name_plural = _("Книги")

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
    year_release = models.PositiveSmallIntegerField(
        verbose_name=_("Год выхода в свет"),
        blank=True,
    )
    copy_count = models.PositiveSmallIntegerField(
        verbose_name=_("Число копий"),
        default=1,
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name=_("Цена"),
    )
    author = models.ForeignKey(
        "p_library.Author",
        verbose_name=_("Автор"),        
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="book_author",
    )
    publisher = models.ForeignKey(
        "p_library.Publisher",
        verbose_name=_("Издательство"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,        
        related_name="books",
    )
    year_publishing = models.PositiveIntegerField(
        verbose_name=_("Год издания"),
        blank=True,
    )
    readers = models.ManyToManyField(
        "p_library.Reader",
        through='BookReader',
        symmetrical=False,
        verbose_name=_("Сейчас читают"),
        related_name="reading_books",
        blank=True,
    )

    def get_absolute_url(self):
        return reverse_lazy('p_library:view_book', kwargs={'pk': self.pk})

    def __str__(self):
        return Template('$title').substitute(title=self.title)


class Publisher(models.Model):
    class Meta:
        verbose_name = _("Издательство")
        verbose_name_plural = _("Издательства")

    name = models.TextField(
        verbose_name=_("Издательство"),
        default=_("Неизвестно"),
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
        return reverse_lazy('p_library:view_publisher', kwargs={'pk': self.pk})    

    def __str__(self):
        return Template('$name').substitute(name=self.name)


class Reader(models.Model):
    class Meta:
        verbose_name = _("Читатель")
        verbose_name_plural = _("Читатели")

    name = models.TextField(
        verbose_name=_("Читатель"),
    )
    address = models.TextField(
        verbose_name=_("Адрес"),
        default=_("Планета Земля"),
    )

    def get_absolute_url(self):
        return reverse_lazy('p_library:view_reader', kwargs={'pk': self.pk})

    def __str__(self):
        return Template('$name').substitute(name=self.name)


class BookReader(models.Model):
    book = models.ForeignKey(
        Book,
        verbose_name=_("Сейчас читает:"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="book_reading_reader",
    )
    reader = models.ForeignKey(
        Reader,
        verbose_name=_("Эту книгу сейчас читают:"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="reader_reading_book",
    )
    borrow_date = models.DateField(
        verbose_name=_("Дата"),
        null=True,
        blank=True,
        auto_now=True,
    )

    def save(self, *args, **kwargs):
        if BookReader.objects.filter(book_id=self.book_id).count() < self.book.copy_count:
            super(BookReader, self).save(*args, **kwargs)  # Call the "real" save() method
        else:
            #raise ValidationError("К сожалению, все копии книги на руках. Зайдите попозже :)")
            return # Do nothing
