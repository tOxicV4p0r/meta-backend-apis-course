# Generated by Django 4.2.2 on 2023-06-20 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LittlelemonAPI', '0012_alter_ratinguss_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratinguss',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
