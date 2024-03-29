# Generated by Django 2.2.2 on 2019-06-10 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=30),
        ),
    ]
