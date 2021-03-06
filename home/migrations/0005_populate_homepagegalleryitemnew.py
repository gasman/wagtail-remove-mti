# Generated by Django 3.0.11 on 2020-11-06 15:24

from django.db import migrations
import json


def populate_homepagegalleryitemnew(apps, schema_editor):
    HomePageGalleryItem = apps.get_model("home", "HomePageGalleryItem")
    HomePageGalleryItemNew = apps.get_model("home", "HomePageGalleryItemNew")
    HomePage = apps.get_model("home", "HomePage")

    id_mapping = {}
    for old_item in HomePageGalleryItem.objects.all():
        new_item = HomePageGalleryItemNew.objects.create(
            sort_order=old_item.sort_order,
            name=old_item.name,
            page_id=old_item.page_id
        )
        id_mapping[old_item.pk] = new_item.pk

    # also update gallery_items IDs in homepage revisions
    for page in HomePage.objects.all():
        for revision in page.revisions.all():
            revision_data = json.loads(revision.content_json)
            if 'gallery_items' in revision_data:
                gallery_items_new = []
                for item in revision_data['gallery_items']:
                    item_copy = item.copy()
                    if item['pk'] in id_mapping:
                        item_copy['pk'] = id_mapping[item['pk']]
                        gallery_items_new.append(item_copy)
                revision_data['gallery_items'] = gallery_items_new
                revision.content_json = json.dumps(revision_data)
                revision.save()


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepagegalleryitemnew'),
    ]

    operations = [
        migrations.RunPython(populate_homepagegalleryitemnew),
    ]
