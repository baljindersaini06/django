# Generated by Django 2.2.2 on 2019-06-21 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0030_aboutdis_div_clas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutdis',
            name='div_clas',
            field=models.CharField(choices=[('col-lg-6 wow fadeInUp pt-5 pt-lg-0', 'left'), ('col-lg-6 wow fadeInUp pt-4 pt-lg-0 order-2 order-lg-1', 'right')], max_length=60),
        ),
    ]