# Generated by Django 5.1 on 2024-08-29 22:18

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_delete_cartitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
