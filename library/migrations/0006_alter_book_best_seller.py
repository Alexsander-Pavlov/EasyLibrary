# Generated by Django 5.0.7 on 2024-08-14 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_book_quantity_order_requestextension'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='best_seller',
            field=models.BooleanField(default=False, help_text='Является ли книга лидером продаж', verbose_name='лидер продаж'),
        ),
    ]
