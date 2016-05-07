# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=100)),
                ('phone', models.IntegerField(unique=True, max_length=10)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
