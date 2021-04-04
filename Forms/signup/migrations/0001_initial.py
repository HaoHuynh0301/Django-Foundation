# Generated by Django 3.1.7 on 2021-04-03 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.IntegerField(max_length=12)),
            ],
        ),
    ]