from django import template

from ..models import Menu

register = template.Library()


@register.simple_tag()
def get_menu(slug):
    try:
        return Menu.objects.get(slug=slug)
    # slug under Menu class in models.py = slug parameter in this function
    except Menu.DoesNotExist:
        return Menu.objects.none()
