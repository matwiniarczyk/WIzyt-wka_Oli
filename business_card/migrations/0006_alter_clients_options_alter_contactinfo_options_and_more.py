# Generated by Django 5.1.6 on 2025-03-13 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business_card', '0005_remove_serviceoffer_image_alter_clients_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clients',
            options={'verbose_name': 'Klient', 'verbose_name_plural': 'Klienci'},
        ),
        migrations.AlterModelOptions(
            name='contactinfo',
            options={'verbose_name': 'Wiadomość', 'verbose_name_plural': 'Wiadomości'},
        ),
        migrations.AlterModelOptions(
            name='maininfoabout',
            options={'verbose_name': 'Główne info', 'verbose_name_plural': 'Główne info'},
        ),
        migrations.AlterModelOptions(
            name='serviceoffer',
            options={'verbose_name': 'Usługa', 'verbose_name_plural': 'Usługi'},
        ),
    ]
