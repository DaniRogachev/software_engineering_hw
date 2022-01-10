# Generated by Django 3.1.1 on 2021-11-23 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elsys', '0003_alter_car_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='is_electric',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
