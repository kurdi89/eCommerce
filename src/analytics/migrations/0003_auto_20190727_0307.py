# Generated by Django 2.2.3 on 2019-07-27 00:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_usersession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectviewed',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='objectviewed',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usersession',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
