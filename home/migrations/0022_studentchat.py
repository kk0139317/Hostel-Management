# Generated by Django 4.0.4 on 2022-04-22 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_complain'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.CharField(max_length=50)),
                ('msg', models.CharField(max_length=50)),
                ('Aaa', models.CharField(max_length=50, null=True)),
                ('Bbb', models.CharField(max_length=50, null=True)),
                ('Ccc', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
