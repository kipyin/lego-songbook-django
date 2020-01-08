# Generated by Django 3.0.1 on 2020-01-08 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='key',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='sheet_type',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
