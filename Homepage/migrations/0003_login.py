# Generated by Django 4.0.1 on 2022-04-17 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0002_remove_hot_tour_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Login')),
            ],
        ),
    ]
