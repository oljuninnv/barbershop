# Generated by Django 4.2.3 on 2024-06-26 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_visiting_service_visiting_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='photo',
            field=models.ImageField(blank=True, help_text='Загрузите фото работника', null=True, upload_to='worker_photos', verbose_name='Фото'),
        ),
    ]
