from django import template

register = template.Library()

@register.filter
def replace(string):
    return string.replace(' ', '-')
