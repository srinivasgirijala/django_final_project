# Generated by Django 3.1.7 on 2021-07-14 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appli',
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
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
