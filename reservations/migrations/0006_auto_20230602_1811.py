# Generated by Django 3.0.7 on 2023-06-02 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0005_auto_20230602_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='reservation_status',
            field=models.CharField(choices=[('FREE', 'FREE'), ('RESERVED', 'RESERVED'), ('BOOKED', 'BOOKED')], default='FREE', max_length=8),
        ),
        migrations.AlterField(
            model_name='reservedseat',
            name='seat_type',
            field=models.CharField(choices=[('STANDARD', 'STANDARD'), ('VIP', 'VIP')], default='STANDARD', max_length=8),
        ),
    ]
