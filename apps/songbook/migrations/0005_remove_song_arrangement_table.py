# Generated by Django 3.0.3 on 2020-02-06 02:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("songbook", "0004_set_position_assignment_person_position_unique_together"),
    ]

    operations = [
        migrations.RenameField(
            model_name="song", old_name="original_key", new_name="key",
        ),
        migrations.RemoveField(model_name="plan", name="song_arrangements",),
        migrations.AddField(
            model_name="plan",
            name="songs",
            field=models.ManyToManyField(related_name="plans", to="songbook.Song"),
        ),
        migrations.AddField(
            model_name="song",
            name="bpm",
            field=models.IntegerField(blank=True, null=True, verbose_name="BPM"),
        ),
        migrations.AddField(
            model_name="song",
            name="meter",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.RemoveField(model_name="plan", name="team_arrangement",),
        migrations.AddField(
            model_name="plan",
            name="team_arrangement",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="plans",
                to="songbook.TeamArrangement",
            ),
        ),
        migrations.DeleteModel(name="SongArrangement",),
    ]