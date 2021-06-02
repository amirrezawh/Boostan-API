# Generated by Django 3.2.3 on 2021-05-27 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessorStatic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('behavior', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('professorstatic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Vote.professorstatic')),
                ('respect', models.IntegerField(default=0)),
                ('teach', models.IntegerField(default=0)),
                ('course', models.ManyToManyField(to='Vote.Course')),
            ],
            bases=('Vote.professorstatic',),
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respect', models.IntegerField(default=0)),
                ('teach', models.IntegerField(default=0)),
                ('behavior', models.IntegerField(default=0)),
                ('course', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Vote.course')),
                ('student', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote', to='Vote.professor')),
            ],
        ),
    ]
