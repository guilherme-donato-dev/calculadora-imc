# Generated by Django 5.1.3 on 2024-11-23 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imc', '0002_calculadoraimc_delete_imc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculadoraimc',
            name='altura',
            field=models.FloatField(max_length=10),
        ),
        migrations.AlterField(
            model_name='calculadoraimc',
            name='peso',
            field=models.FloatField(max_length=10),
        ),
    ]
