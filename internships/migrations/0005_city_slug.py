# Generated by Django 2.0.6 on 2018-07-02 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internships', '0004_auto_20180701_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='slug',
            field=models.SlugField(default='test'),
        ),
    ]
