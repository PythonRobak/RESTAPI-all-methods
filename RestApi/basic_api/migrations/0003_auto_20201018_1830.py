# Generated by Django 3.0 on 2020-10-18 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_api', '0002_article_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='date',
            new_name='date_created',
        ),
        migrations.AddField(
            model_name='article',
            name='date_edited',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
