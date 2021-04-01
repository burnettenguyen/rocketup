from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register
)
from .models import Testimonials


# Register your models here.
@modeladmin_register
class TestimonialAdmin(ModelAdmin):
    """Testimonial admin"""

    model = Testimonials
    menu_label = "Testimonials"
    menu_icon = "placeholder"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("quote", "attribution")
    # indicates how it is displayed in list within admin to be sortable
    search_fields = ("quote", "attribution")
    # put in what fields to search for
