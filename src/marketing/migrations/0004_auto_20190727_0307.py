# Generated by Django 2.2.3 on 2019-07-27 00:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0003_auto_20171018_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketingpreference',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
