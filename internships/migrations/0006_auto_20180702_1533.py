# Generated by Django 2.0.6 on 2018-07-02 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internships', '0005_city_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.SlugField(),
        ),
    ]