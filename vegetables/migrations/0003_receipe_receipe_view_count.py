# Generated by Django 4.2.10 on 2024-03-09 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegetables', '0002_receipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='receipe_view_count',
            field=models.IntegerField(default=0),
        ),
    ]