# Generated by Django 4.0.1 on 2022-01-21 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='place',
            field=models.CharField(default='malappuram', max_length=100),
            preserve_default=False,
        ),
    ]