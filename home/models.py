from __future__ import absolute_import, unicode_literals

from django.db import models
from wagtail.core.models import Orderable
from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.core.models import Page


class HomePage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('gallery_items', label="Gallery items"),
    ]


class GalleryItem(Orderable):
    name = models.CharField(max_length=255)

    panels = [
        FieldPanel('name')
    ]

class GalleryItemAbstract(Orderable):
    name = models.CharField(max_length=255)

    panels = [
        FieldPanel('name')
    ]

    class Meta(Orderable.Meta):
        abstract = True


class HomePageGalleryItem(GalleryItem):
    page = ParentalKey('home.HomePage', related_name='gallery_items')


class HomePageGalleryItemNew(GalleryItemAbstract):
    page = ParentalKey('home.HomePage', related_name='gallery_items_new')
