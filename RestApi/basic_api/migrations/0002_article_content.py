# Generated by Django 3.0 on 2020-10-17 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]