# Generated by Django 3.0.7 on 2023-06-02 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_halls', '0004_auto_20230602_1613'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cinemahall',
            options={'ordering': ['-id_hall']},
        ),
    ]
