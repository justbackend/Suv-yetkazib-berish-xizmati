# Generated by Django 4.2.7 on 2023-11-03 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='ish_vaqti',
            field=models.CharField(max_length=15),
        ),
    ]
