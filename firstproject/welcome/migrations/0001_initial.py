# Generated by Django 4.0.1 on 2022-01-21 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('car', models.CharField(max_length=100)),
                ('cmp', models.CharField(max_length=100)),
            ],
        ),
    ]
