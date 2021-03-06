# Generated by Django 2.1.5 on 2019-03-21 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enter_time', models.DateTimeField(verbose_name='Enter Time')),
                ('leave_time', models.DateTimeField(verbose_name='Leave Time')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Room')),
            ],
        ),
    ]
