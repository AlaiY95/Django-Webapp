# Generated by Django 4.0.2 on 2022-02-24 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myapp',
            name='url',
        ),
    ]
