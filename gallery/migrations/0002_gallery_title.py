# Generated by Django 2.0.2 on 2018-06-05 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='title',
            field=models.CharField(default=2, max_length=2000),
            preserve_default=False,
        ),
    ]
