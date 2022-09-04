from django import template
from p_library.models import *

register = template.Library()


@register.simple_tag()
def get_books():
    return Book.objects.all()

@register.simple_tag()
def get_books_None_author():
    return Book.objects.filter(author=None)

@register.simple_tag()
def get_books_None_publisher():
    return Book.objects.filter(publisher=None)         

@register.simple_tag()
def get_authors():
    return Author.objects.all()

@register.simple_tag()
def get_publishers():
    return Publisher.objects.all()

@register.simple_tag()
def get_readers():
    return Reader.objects.all()
