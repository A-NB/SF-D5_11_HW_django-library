from django import template

register = template.Library()

@register.filter(name='divide')
def divide(dividend, divisor):
    if dividend % divisor == 0:
        return True
    return False