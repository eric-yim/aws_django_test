# Generated by Django 3.0.8 on 2020-07-29 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_project_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(default='ML', max_length=32),
        ),
    ]