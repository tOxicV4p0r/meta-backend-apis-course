# Generated by Django 4.2.2 on 2023-06-20 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittlelemonAPI', '0003_booker_remove_book_littlelemon_price_f5581b_idx_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['price'], name='Littlelemon_price_f5581b_idx'),
        ),
    ]