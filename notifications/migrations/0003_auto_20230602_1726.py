# Generated by Django 3.0.7 on 2023-06-02 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20230602_1615'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailnotification',
            options={'ordering': ['-send_date']},
        ),
        migrations.RenameField(
            model_name='emailnotification',
            old_name='Subject',
            new_name='subject',
        ),
    ]
