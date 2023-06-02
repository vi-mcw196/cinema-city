# Generated by Django 3.0.7 on 2023-06-02 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20230602_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[(1, 'HORROR'), (2, 'ACTION'), (3, 'COMEDY'), (4, 'DRAMA'), (5, 'ROMANCE')], default=3, max_length=15),
        ),
        migrations.AlterField(
            model_name='movie',
            name='id_movie',
            field=models.AutoField(db_index=True, primary_key=True, serialize=False),
        ),
    ]
