# Generated by Django 4.2.2 on 2023-06-20 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittlelemonAPI', '0011_ratinguss_user_alter_ratinguss_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratinguss',
            name='user',
            field=models.CharField(max_length=255),
        ),
    ]