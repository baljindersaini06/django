# Generated by Django 2.2.2 on 2019-06-20 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20190620_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='team_work',
        ),
    ]