# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=120, null=True, blank=True)),
                ('image', models.ImageField(default=b'', upload_to=b'category/images')),
                ('description', models.TextField(null=True, blank=True)),
                ('slug', models.SlugField(default=b'', unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('image', models.ImageField(default=b'', upload_to=b'products/images')),
                ('slug', models.SlugField(unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'products/images')),
                ('thumbnail', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('products', models.ForeignKey(blank=True, to='testapp.Product', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategoryChild',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sub_cat_child_name', models.CharField(max_length=120, null=True, blank=True)),
                ('image', models.ImageField(default=b'', upload_to=b'products/images')),
                ('description', models.TextField(null=True, blank=True)),
                ('slug', models.SlugField(default=b'', unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategoryParent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sub_cat_parent_name', models.CharField(max_length=120, null=True, blank=True)),
                ('image', models.ImageField(default=b'', upload_to=b'subcategoryparent/images')),
                ('description', models.TextField(null=True, blank=True)),
                ('slug', models.SlugField(default=b'', unique=True)),
                ('active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, to='testapp.Category', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='subcategorychild',
            name='sub_category_parent',
            field=models.ForeignKey(blank=True, to='testapp.SubCategoryParent', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category_child',
            field=models.ForeignKey(to='testapp.SubCategoryChild'),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([('title', 'slug')]),
        ),
    ]
