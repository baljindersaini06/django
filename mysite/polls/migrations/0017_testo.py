# Generated by Django 2.2.2 on 2019-06-20 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_auto_20190620_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tes_name', models.CharField(max_length=50)),
                ('tes_designation', models.CharField(max_length=50)),
                ('tes_des', models.TextField()),
            ],
        ),
    ]
