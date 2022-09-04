from django import template

register = template.Library()

# @register.simple_tag
# def diapason(stop):
#     return range(stop)


@register.filter(name='diapason')
def diapason(_min, args=None):
    _max, _step = None, None
    if args:
        if not isinstance(args, int):
            _max, _step = map(int, args.split(','))
        else:
            _max = args
    args = filter(None, (_min, _max, _step))
    return range(*args)    