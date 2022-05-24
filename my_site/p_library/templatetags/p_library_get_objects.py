from django import template
from p_library.models import *

register = template.Library()


@register.simple_tag()
def get_books():
    return Book.objects.all()


@register.simple_tag()
def get_authors():
    return Author.objects.all()


@register.simple_tag()
def get_publishers():
    return PublishingHouse.objects.all()


@register.simple_tag()
def get_friends():
    return Friend.objects.all()
