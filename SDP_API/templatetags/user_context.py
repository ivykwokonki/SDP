from django import template
from django.contrib.auth.models import Group, User

register = template.Library()

@register.filter(name='has_group')
def has_group(user, groupID):
    if user.groups.filter(id=groupID):
        return True
    else:
        return False