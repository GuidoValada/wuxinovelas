# Generated by Django 3.0.1 on 2020-04-28 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('novelas', '0007_auto_20200426_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='chapter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='novelas.allchaps'),
        ),
        migrations.AlterField(
            model_name='novelas',
            name='categoria',
            field=models.CharField(choices=[('NC', 'Novela China'), ('NJ', 'Novela Japonesa'), ('NK', 'Novela Koreana')], max_length=50),
        ),
    ]
