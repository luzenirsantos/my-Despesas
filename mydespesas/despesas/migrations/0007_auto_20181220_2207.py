# Generated by Django 2.1.4 on 2018-12-21 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despesas', '0006_auto_20181220_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='vencimento',
            field=models.DateTimeField(),
        ),
    ]
