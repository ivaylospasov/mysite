from django import template

register = template.Library()

@register.filter('cut')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string.
    """
    return value.join(arg.split())


@register.filter('space_comma')
def space_comma(value, arg):
    """
    places space after comma.
    """
    return value.replace(arg, ', ')


register.filter('double_br')
def double_br(value, arg):
    """
    places space after comma.
    """
    return value.replace(arg, '<br /><br />')
