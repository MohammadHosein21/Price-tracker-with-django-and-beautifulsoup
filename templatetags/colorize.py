from django.utils.safestring import mark_safe
from django import template

register = template.Library()

@register.filter
def colorize(value):
    mark = str(value)[:1]
    if mark == '-':
        html_string = f"<span style='color:green'>{value}</span>"
    elif mark == "0":
        html_string = f"<span style='color:blue'>{value}</span>"
    else:
        html_string = f"<span style='color:red'>{value}</span>"
    return mark_safe(html_string)