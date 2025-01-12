# Generated by Django 5.1.4 on 2025-01-11 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('c_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=256)),
                ('c_surname', models.CharField(max_length=256)),
                ('c_email', models.EmailField(max_length=256)),
                ('c_number', models.CharField(max_length=256)),
                ('c_message', models.TextField(max_length=1000)),
            ],
        ),
    ]