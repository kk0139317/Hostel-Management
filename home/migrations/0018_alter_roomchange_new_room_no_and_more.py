# Generated by Django 4.0.4 on 2022-04-21 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_roomchange'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomchange',
            name='new_room_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='roomchange',
            name='old_room_no',
            field=models.IntegerField(),
        ),
    ]
