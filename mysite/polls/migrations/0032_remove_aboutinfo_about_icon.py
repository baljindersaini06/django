# Generated by Django 2.2.2 on 2019-06-21 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0031_auto_20190621_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutinfo',
            name='About_icon',
        ),
    ]
