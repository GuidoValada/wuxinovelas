# Generated by Django 3.0.1 on 2020-04-21 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('novelas', '0002_auto_20200112_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='novelas',
            name='img',
        ),
        migrations.AddField(
            model_name='allchaps',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='chapter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='novelas.allchaps'),
        ),
    ]
