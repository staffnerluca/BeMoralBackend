# Generated by Django 5.0.7 on 2024-08-28 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='course_images/'),
        ),
    ]
