# Generated by Django 3.1.7 on 2021-04-07 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
    ]
