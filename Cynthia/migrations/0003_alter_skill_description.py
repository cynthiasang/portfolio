# Generated by Django 4.0.4 on 2022-06-11 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cynthia', '0002_skill_description_skill_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
