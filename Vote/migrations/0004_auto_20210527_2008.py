# Generated by Django 3.2.3 on 2021-05-27 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vote', '0003_auto_20210527_2006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professorstatic',
            name='course',
        ),
        migrations.AddField(
            model_name='professorstatic',
            name='course',
            field=models.ManyToManyField(to='Vote.Course'),
        ),
    ]
