# Generated by Django 4.2.3 on 2024-06-28 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_visiting_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visiting',
            name='time',
            field=models.TimeField(blank=True, help_text='Выберите время приёма', null=True, verbose_name='Время'),
        ),
    ]
