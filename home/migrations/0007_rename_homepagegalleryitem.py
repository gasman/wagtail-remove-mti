# Generated by Django 3.0.11 on 2020-11-06 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_delete_old_homepagegalleryitem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomePageGalleryItemNew',
            new_name='HomePageGalleryItem',
        ),
    ]
