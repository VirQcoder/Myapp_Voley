# Generated by Django 4.1.5 on 2023-05-12 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volleyapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='photo',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
