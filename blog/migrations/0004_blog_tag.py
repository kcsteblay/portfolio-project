# Generated by Django 2.0.2 on 2018-06-02 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180602_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
