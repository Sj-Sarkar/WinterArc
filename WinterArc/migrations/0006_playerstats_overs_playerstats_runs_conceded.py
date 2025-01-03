# Generated by Django 4.2.4 on 2025-01-02 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WinterArc', '0005_alter_pendingregistration_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerstats',
            name='overs',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='playerstats',
            name='runs_conceded',
            field=models.IntegerField(default=0),
        ),
    ]
