# Generated by Django 2.2.2 on 2019-08-07 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encurtador', '0002_url_shortcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='shortcode',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
