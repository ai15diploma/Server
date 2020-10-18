# Generated by Django 3.0.3 on 2020-05-21 16:12

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('route', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.TextField()),
                ('Statist', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayOff', models.BooleanField(blank=True)),
                ('departure', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=5), blank=True, size=None)),
                ('arrival', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=5), blank=True, size=None)),
                ('routeId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='route.Route')),
            ],
        ),
    ]
