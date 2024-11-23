# Generated by Django 5.1.3 on 2024-11-23 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='calculadoraIMC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('altura', models.FloatField(help_text='Altura em metros...')),
                ('peso', models.FloatField(help_text='Peso em kg...')),
                ('imc', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='IMC',
        ),
    ]