from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.blocks import SnippetChooserBlock

from streams import blocks


NEW_TABLE_OPTIONS = {
    'minSpareRows': 0,
    'startRows': 4,
    'startCols': 4,
    'colHeaders': False,
    'rowHeaders': True,
    'contextMenu': [
        'row_above',
        'row_below',
        '---------',
        'col_left',
        'col_right',
        '---------',
        'remove_row',
        'remove_col',
        '---------',
        'undo',
        'redo'
    ],
    'editor': 'text',
    'stretchH': 'all',
    'renderer': 'text',
    'autoColumnSize': False,
}


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
        ("image_and_text", blocks.ImageAndTextBlock()),
        ("cta", blocks.CallToActionBlock()),
        ("testimonial", SnippetChooserBlock(
            target_model='testimonials.Testimonials',
            template="streams/testimonial_block.html",
        )),
        ("pricing_table_block", blocks.PricingTableBlock()),
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

