# Generated by Django 4.1.5 on 2023-01-18 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0004_alter_pokemon_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
