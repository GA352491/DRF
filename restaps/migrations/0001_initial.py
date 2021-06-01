# Generated by Django 3.2.3 on 2021-05-31 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('language', models.CharField(blank=True, max_length=120, null=True)),
                ('genre', models.CharField(blank=True, max_length=120, null=True)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
