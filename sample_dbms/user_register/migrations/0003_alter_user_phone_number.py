# Generated by Django 4.1.7 on 2023-06-12 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_register', '0002_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
