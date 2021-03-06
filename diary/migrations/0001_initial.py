# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(default='', blank=True, max_length=100)),
                ('entry', models.TextField()),
                ('hash', models.TextField()),
                ('owner', models.ForeignKey(related_name='entries', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
