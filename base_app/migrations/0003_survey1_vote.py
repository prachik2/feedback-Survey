# Generated by Django 2.1.3 on 2019-07-18 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_survey1'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey1',
            name='vote',
            field=models.IntegerField(default=1),
        ),
    ]
