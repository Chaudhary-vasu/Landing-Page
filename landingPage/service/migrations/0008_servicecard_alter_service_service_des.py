# Generated by Django 4.1.7 on 2023-03-29 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_delete_servicecards'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicecard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_card_title', models.CharField(max_length=50)),
                ('service_card_intro', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='service',
            name='service_des',
            field=models.TextField(),
        ),
    ]