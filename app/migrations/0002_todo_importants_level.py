# Generated by Django 5.0.3 on 2024-04-15 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='importants_level',
            field=models.IntegerField(default=0),
        ),
    ]