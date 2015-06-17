# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lenguaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=120)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='subcategoria',
            name='foranea_tipo',
            field=models.ForeignKey(to='datos.Tipo'),
        ),
        migrations.AddField(
            model_name='lenguaje',
            name='foranea_subcat',
            field=models.ForeignKey(to='datos.Subcategoria'),
        ),
        migrations.AddField(
            model_name='lenguaje',
            name='foranea_tipo',
            field=models.ForeignKey(to='datos.Tipo'),
        ),
    ]
