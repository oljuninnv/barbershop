# Generated by Django 4.2.3 on 2024-06-27 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_visiting_customer_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visiting',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Введите итоговую стоимость за приём', max_digits=8, null=True, verbose_name='Итоговая цена'),
        ),
    ]
