# Generated by Django 3.0.1 on 2020-01-31 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='songbook.Team'),
        ),
    ]