# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 17:05
from __future__ import unicode_literals

from django.db import migrations, models


def forwards(apps, schema_editor):
    Order = apps.get_model('pretixbase', 'Order')
    for o in Order.objects.all():
        for i, p in enumerate(o.positions.all()):
            p.positionid = i + 1
            p.save()


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0049_checkin'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderposition',
            name='positionid',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.RunPython(
            forwards, migrations.RunPython.noop
        ),
    ]