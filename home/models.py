from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks


class HomePage(Page):

    template = 'home/home_page.html'

    lead_subtitle = models.CharField(
        max_length=20,
        blank=True,
        # Field can be left blank
        help_text = "Subheading under banner title",
    )

    lead_text = models.CharField(
        max_length=100,
        blank=True,
        # Field can be left blank
        help_text="Subtext under banner title",
    )

    button = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        # Field can be null
        related_name="+",
        help_text='Select an optional page to link to',
        on_delete=models.SET_NULL,
    )

    button_text = models.CharField(
        max_length=50,
        blank=True,
        help_text='Button Text',
    )

    banner_background_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        related_name="+",
        help_text="The banner background image",
        on_delete=models.SET_NULL,
    )

    body = StreamField([
        ("title", blocks.TitleBlock()),
        ("cards", blocks.CardsBlock()),
        ("image_and_text", blocks.ImageAndTextBlock())
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("lead_subtitle"),
        FieldPanel("lead_text"),
        PageChooserPanel("button"),
        FieldPanel("button_text"),
        ImageChooserPanel("banner_background_image"),
        StreamFieldPanel("body"),
    ]

