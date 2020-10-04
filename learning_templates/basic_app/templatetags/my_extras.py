from django import template

register = template.Library()


@register.filter(name='my_tag')
def my_tag(value, arg):
    """
    This  cuts out all the values of "arg" from the string
    """
    return value.replace(arg, '')


# register.filter('my_tag', my_tag)
