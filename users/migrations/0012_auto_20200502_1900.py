# Generated by Django 3.0.1 on 2020-05-02 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novelas', '0012_auto_20200502_1900'),
        ('users', '0011_auto_20200502_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='historial',
            field=models.ManyToManyField(to='novelas.allchaps'),
        ),
    ]
