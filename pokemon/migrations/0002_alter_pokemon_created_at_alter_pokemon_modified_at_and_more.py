# Generated by Django 4.0.4 on 2023-01-18 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='name_ar',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='name_fr',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='name_jp',
            field=models.CharField(default='', max_length=30),
        ),
    ]
