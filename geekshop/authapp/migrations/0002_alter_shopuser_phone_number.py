# Generated by Django 3.2.9 on 2022-01-02 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=14, verbose_name='Номер телефона'),
        ),
    ]
