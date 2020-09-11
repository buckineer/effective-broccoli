# Generated by Django 3.0.7 on 2020-06-18 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.CharField(max_length=150)),
                ('club', models.CharField(max_length=150)),
                ('date', models.DateTimeField(verbose_name='date scraped')),
                ('field_position', models.CharField(max_length=10)),
                ('nationality', models.CharField(max_length=150)),
                ('sentiment_score', models.FloatField()),
                ('n_positive', models.IntegerField()),
                ('n_negative', models.IntegerField()),
                ('n_neutral', models.IntegerField()),
                ('total_reviews', models.IntegerField()),
            ],
            options={
                'ordering': ['date', 'player', 'sentiment_score'],
            },
        ),
    ]
