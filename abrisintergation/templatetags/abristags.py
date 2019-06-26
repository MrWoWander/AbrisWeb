import json

from django import template

register = template.Library()


@register.filter
def field_format(value):
    json1_data = json.loads(value)
    return json1_data['f1']
