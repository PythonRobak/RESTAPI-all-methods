# Generated by Django 3.0 on 2020-10-18 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_api', '0003_auto_20201018_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_edited',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
