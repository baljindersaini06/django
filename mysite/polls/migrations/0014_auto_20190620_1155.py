# Generated by Django 2.2.2 on 2019-06-20 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20190620_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_work',
            field=models.CharField(default='hello', max_length=500),
        ),
    ]
