# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-14 04:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book_chapter',
            options={'verbose_name': '章节信息', 'verbose_name_plural': '章节信息'},
        ),
        migrations.AlterModelOptions(
            name='book_classify2',
            options={'verbose_name': '书籍类别', 'verbose_name_plural': '书籍类别'},
        ),
    ]
