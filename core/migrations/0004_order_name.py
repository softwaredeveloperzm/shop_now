# Generated by Django 5.0.6 on 2024-07-27 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_order_transction_id_order_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
