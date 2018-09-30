# Generated by Django 2.1.1 on 2018-09-25 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('venue', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]
