# Generated by Django 2.0.4 on 2018-05-31 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_remove_article_article_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
