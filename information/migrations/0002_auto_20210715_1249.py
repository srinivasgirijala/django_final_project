# Generated by Django 3.1.7 on 2021-07-15 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appli',
        ),
        migrations.DeleteModel(
            name='feedback',
        ),
        migrations.DeleteModel(
            name='subscribers',
        ),
    ]
