# Generated by Django 3.2.4 on 2021-06-07 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_post_header_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, default='fox.jpeg', null=True, upload_to='images/'),
        ),
    ]
