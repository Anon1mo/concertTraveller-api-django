# Generated by Django 2.1.1 on 2018-09-25 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=255)),
                ('maxNumUsers', models.IntegerField(default=0)),
                ('eventId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='events.Event')),
                ('ownerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
                ('users', models.ManyToManyField(related_name='offers', to='users.User')),
            ],
        ),
        migrations.AddField(
            model_name='chat',
            name='offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offers.Offer'),
        ),
    ]
