# Generated by Django 5.0.3 on 2024-06-11 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_songs_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='file',
            field=models.FileField(upload_to='app/songs/'),
        ),
    ]
