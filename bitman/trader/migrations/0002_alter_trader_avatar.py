# Generated by Django 4.0.3 on 2022-04-23 21:05

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trader',
            name='avatar',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='users/'),
        ),
    ]
