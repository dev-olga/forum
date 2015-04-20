from forum.view_decorators.show_view import show_category
from django import template
register = template. Library()

@register.filter(name='filter_by_permissions')
def filter_by_permissions(categories, user):
    return (c for c in categories if show_category(c, user))