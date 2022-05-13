# Generated by Django 3.2.8 on 2021-11-01 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0030_auto_20211101_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers',
            name='followed',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='user_followed', to=settings.AUTH_USER_MODEL),
        ),
    ]
