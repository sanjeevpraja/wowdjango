# Generated by Django 4.2.2 on 2023-07-08 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='group',
        ),
    ]
