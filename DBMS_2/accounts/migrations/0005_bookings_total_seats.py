# Generated by Django 3.2.9 on 2021-12-06 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_movie_movie_rdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='total_seats',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
