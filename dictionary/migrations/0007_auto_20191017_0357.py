# Generated by Django 2.2.5 on 2019-10-17 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0006_auto_20191017_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordpart',
            name='gloss',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='wordpart',
            name='subtypes',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='wordpart',
            name='title',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='wordpart',
            name='type',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]