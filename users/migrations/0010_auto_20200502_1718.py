# Generated by Django 3.0.1 on 2020-05-02 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novelas', '0010_auto_20200502_1718'),
        ('users', '0009_auto_20200501_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='historial',
            field=models.ManyToManyField(to='novelas.allchaps'),
        ),
    ]