# Generated by Django 2.0.4 on 2018-05-31 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20180531_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_date',
            field=models.DateTimeField(),
        ),
    ]