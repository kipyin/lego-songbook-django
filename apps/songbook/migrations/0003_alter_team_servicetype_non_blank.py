# Generated by Django 3.0.1 on 2020-01-31 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songbook', '0002_alter_position_team_non_blank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='service_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='songbook.ServiceType'),
        ),
    ]