# Generated by Django 5.1.3 on 2024-11-23 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IMC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('altura', models.FloatField(max_length=5)),
                ('peso', models.FloatField(max_length=10)),
            ],
        ),
    ]
