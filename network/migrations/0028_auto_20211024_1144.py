# Generated by Django 3.2.8 on 2021-10-24 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0027_auto_20211024_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='followers',
            name='followed',
        ),
        migrations.AddField(
            model_name='followers',
            name='followed',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='user_followed', to=settings.AUTH_USER_MODEL),
        ),
    ]
