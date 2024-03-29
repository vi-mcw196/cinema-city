# Generated by Django 3.0.7 on 2023-06-01 22:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CinemaHall',
            fields=[
                ('id_hall', models.AutoField(primary_key=True, serialize=False)),
                ('hall_number', models.IntegerField()),
                ('max_seats', models.IntegerField()),
                ('rows', models.IntegerField()),
                ('columns', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id_screening', models.AutoField(primary_key=True, serialize=False)),
                ('screening_time', models.DateTimeField()),
                ('id_cinema_hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_halls.CinemaHall')),
                ('id_movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
                ('id_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id_screening'],
            },
        ),
    ]
