# Generated by Django 3.2 on 2021-10-06 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_horaire_heure'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horaireclasse',
            name='destination',
        ),
    ]
