# Generated by Django 4.2 on 2023-08-10 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/sport.jpg', null=True, upload_to='blog/'),
        ),
    ]
