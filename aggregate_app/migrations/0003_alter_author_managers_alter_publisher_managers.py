# Generated by Django 4.0.6 on 2022-07-28 10:20

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('aggregate_app', '0002_alter_book_pubdate'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='author',
            managers=[
                ('custom', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='publisher',
            managers=[
                ('custom', django.db.models.manager.Manager()),
            ],
        ),
    ]
