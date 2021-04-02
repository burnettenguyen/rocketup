"""Flexible page"""

from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

# Create your models here.

class FlexPage(Page):
    """Flexible page class"""



    class Meta:
        template = "flex/flex_page.html"
        verbose_name = "Flex (Misc) Page"
        verbose_name_plural = "Flex (Misc) Pages"

