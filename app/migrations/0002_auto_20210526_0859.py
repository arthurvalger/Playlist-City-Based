# Generated by Django 3.1.7 on 2021-05-26 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='playlist',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='musica',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='temp',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
