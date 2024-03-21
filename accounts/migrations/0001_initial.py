# Generated by Django 5.0.3 on 2024-03-21 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('userType', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
