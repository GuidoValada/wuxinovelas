# Generated by Django 3.0.1 on 2020-04-21 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novelas', '0003_auto_20200421_1722'),
        ('users', '0002_auto_20200112_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='historial',
            field=models.ManyToManyField(to='novelas.allchaps'),
        ),
    ]
