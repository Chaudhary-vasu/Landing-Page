# Generated by Django 4.1.7 on 2023-03-28 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_home_logo_home_home_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_email', models.CharField(max_length=50)),
            ],
        ),
    ]
