# Generated by Django 4.2.2 on 2023-06-20 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittlelemonAPI', '0009_ratinguss_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratinguss',
            name='menuitem_id',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ratinguss',
            name='rating',
            field=models.SmallIntegerField(default=1),
        ),
    ]
