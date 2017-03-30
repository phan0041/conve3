from django import template
from django.utils.timesince import timesince
from datetime import datetime

from django.utils.timezone import activate, localtime
from django.utils import timezone
from django.conf import settings

activate(settings.TIME_ZONE)

register = template.Library()


@register.filter(name='timedelta')
def timedelta(value, arg=None):
    if not value:
        return ''
    if arg:
        cmp = localtime(arg)
    else:
        cmp = localtime(timezone.now())
    if value > cmp:
        return "in %s" % timesince(cmp, value)
    else:
        return "%s ago" % timesince(value, cmp)
