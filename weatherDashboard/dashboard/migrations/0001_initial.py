# Generated by Django 3.2.5 on 2021-08-01 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
