# Generated by Django 4.0.3 on 2022-04-26 14:01

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0003_alter_trader_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trader',
            name='avatar',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, max_length=1000, null=True, upload_to='users/'),
        ),
    ]
