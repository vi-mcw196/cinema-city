# Generated by Django 3.0.7 on 2023-06-02 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.PositiveSmallIntegerField(),
        ),
    ]