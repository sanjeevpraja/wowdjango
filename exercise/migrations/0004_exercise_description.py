# Generated by Django 4.2.1 on 2023-06-24 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0003_exercise_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='description',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]