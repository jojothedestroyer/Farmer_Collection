# Generated by Django 4.2.1 on 2024-05-15 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gcna_data', '0019_dispatch_of_dried_nutmeg_rec_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dispatch_of_green_nutmeg_rec',
            old_name='From_Station',
            new_name='Station',
        ),
        migrations.RemoveField(
            model_name='dispatch_of_green_nutmeg_rec',
            name='To_Station',
        ),
    ]
