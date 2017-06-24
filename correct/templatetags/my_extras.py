from django import template

register = template.Library()

@register.filter('cut')
def cut(valuse, arg):
    """
    This cuts out all values of "arg" from the string.
    """
    return value.join(arg.split())
