# Generated by Django 2.0.2 on 2018-06-02 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180515_0634'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-pub_date']},
        ),
        migrations.AddField(
            model_name='blog',
            name='header_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
