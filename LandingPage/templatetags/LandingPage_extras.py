from django import template
from datetime import date
register = template.Library()


@register.filter(name='dayuntil')
def dayuntil(shipper_date):
    """Removes all values of arg from the given string"""
    return (shipper_date - date.today()).days