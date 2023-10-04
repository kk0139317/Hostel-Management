# Generated by Django 4.0.4 on 2022-04-22 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_roomchange'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.CharField(max_length=50)),
                ('hostel', models.CharField(max_length=20)),
                ('room_no', models.IntegerField()),
                ('student_name', models.CharField(max_length=50)),
                ('dept', models.CharField(max_length=50)),
                ('complain', models.CharField(max_length=50)),
                ('status', models.CharField(default='pending', max_length=20)),
                ('Aaa', models.CharField(max_length=50, null=True)),
                ('Aab', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]