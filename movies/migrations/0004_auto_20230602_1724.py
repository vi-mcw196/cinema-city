# Generated by Django 3.0.7 on 2023-06-02 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20230602_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cast',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(blank=True, choices=[(1, 'HORROR'), (2, 'ACTION'), (3, 'COMEDY'), (4, 'DRAMA'), (5, 'ROMANCE')], default=3, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='producer',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
