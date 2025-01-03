# Generated by Django 4.2.4 on 2025-01-01 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_number', models.IntegerField(unique=True)),
                ('venue', models.CharField(default='Kalpataru Club Playground', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PendingRegistration',
            fields=[
                ('phone', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('profile_photo', models.ImageField(upload_to='profile_photos/')),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerRegistration',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('profile_photo', models.ImageField(upload_to='profile_photos/')),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Scorecard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('innings', models.CharField(choices=[('1st', '1st Innings'), ('2nd', '2nd Innings')], max_length=10)),
                ('runs', models.IntegerField(blank=True, null=True)),
                ('balls', models.IntegerField(blank=True, null=True)),
                ('strike_rate', models.FloatField(blank=True, null=True)),
                ('how_out', models.CharField(blank=True, max_length=100, null=True)),
                ('overs', models.FloatField(blank=True, null=True)),
                ('wickets', models.IntegerField(blank=True, null=True)),
                ('economy', models.FloatField(blank=True, null=True)),
                ('runs_conceded', models.IntegerField(blank=True, null=True)),
                ('submitted', models.BooleanField(default=False)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WinterArc.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WinterArc.playerregistration')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matches_played', models.IntegerField(default=0)),
                ('runs', models.IntegerField(default=0)),
                ('wickets', models.IntegerField(default=0)),
                ('average', models.FloatField(default=0.0)),
                ('economy', models.FloatField(default=0.0)),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='WinterArc.playerregistration')),
            ],
        ),
    ]
