# Generated by Django 4.0.4 on 2022-06-07 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=10000)),
                ('Last_Name', models.CharField(max_length=10000)),
                ('Username', models.CharField(max_length=10000)),
            ],
        ),
    ]