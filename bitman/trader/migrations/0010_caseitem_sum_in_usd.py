# Generated by Django 4.0.4 on 2022-04-28 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0009_case_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='caseitem',
            name='sum_in_usd',
            field=models.FloatField(blank=True, null=True),
        ),
    ]