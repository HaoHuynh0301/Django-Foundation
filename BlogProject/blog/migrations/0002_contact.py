# Generated by Django 3.1.7 on 2021-04-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('phone', models.IntegerField(blank=True, max_length=12, null=True)),
                ('message', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
    ]
