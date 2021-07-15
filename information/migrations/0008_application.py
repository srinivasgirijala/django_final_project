# Generated by Django 3.1.7 on 2021-07-15 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0007_subscribers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('state', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=100)),
                ('textarea', models.CharField(max_length=100)),
            ],
        ),
    ]
