# Generated by Django 3.1.1 on 2021-01-03 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='observations',
            field=models.TextField(default='some observations'),
            preserve_default=False,
        ),
    ]
