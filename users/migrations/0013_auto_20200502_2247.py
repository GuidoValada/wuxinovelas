# Generated by Django 3.0.1 on 2020-05-03 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novelas', '0013_auto_20200502_2247'),
        ('users', '0012_auto_20200502_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='historial',
            field=models.ManyToManyField(to='novelas.allchaps'),
        ),
    ]
