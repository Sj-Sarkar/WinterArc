# Generated by Django 4.2.4 on 2025-01-01 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WinterArc', '0002_alter_playerstats_average_alter_playerstats_economy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerstats',
            name='average',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='economy',
            field=models.FloatField(null=True),
        ),
    ]
