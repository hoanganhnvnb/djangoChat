# Generated by Django 4.1.6 on 2023-02-28 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='is_group_chat',
            field=models.BooleanField(default=False),
        ),
    ]