# Generated by Django 4.2.1 on 2024-06-17 13:40

from django.db import migrations, models
import gcna_data.models


class Migration(migrations.Migration):

    dependencies = [
        ('gcna_data', '0029_other_seasoning_trees_est_production_celery_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citrus_mango_trees',
            name='Nutmeg_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='citrus_mango_trees',
            name='Worker_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='coconut_trees',
            name='Nutmeg_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='coconut_trees',
            name='Worker_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='condition',
            name='Nutmeg_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='condition',
            name='Worker_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='farm_house',
            name='Nutmeg_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='farm_house',
            name='Worker_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='farm_water_source',
            name='Nutmeg_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='farm_water_source',
            name='Worker_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='farmer_info',
            name='Nutmeg_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='farmer_info',
            name='Worker_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='food_safety_and_quality',
            name='Nutmeg_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='food_safety_and_quality',
            name='Worker_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='inspector_symmary',
            name='Nutmeg_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='inspector_symmary',
            name='Worker_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='land_info',
            name='Nutmeg_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='land_info',
            name='Worker_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='land_tenur',
            name='Nutmeg_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='land_tenur',
            name='Worker_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nutmeg_frequency',
            name='Nutmeg_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nutmeg_frequency',
            name='Worker_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nutmeg_land',
            name='Nutmeg_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nutmeg_land',
            name='Worker_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nutmeg_trees',
            name='Nutmeg_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nutmeg_trees',
            name='Worker_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nutmeg_variety',
            name='Nutmeg_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nutmeg_variety',
            name='Worker_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='other_crops',
            name='Nutmeg_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='other_crops',
            name='Worker_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='other_crops_cultivated',
            name='Nutmeg_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='other_crops_cultivated',
            name='Worker_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='other_seasoning_trees',
            name='Nutmeg_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='other_seasoning_trees',
            name='Worker_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='other_spices_trees',
            name='Nutmeg_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='other_spices_trees',
            name='Worker_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='policy',
            name='Nutmeg_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='policy',
            name='Worker_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='potential_risks',
            name='Nutmeg_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='potential_risks',
            name='Worker_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='road_access',
            name='Nutmeg_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='road_access',
            name='Worker_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visit',
            name='Land_ID_N0',
            field=models.CharField(blank=True, default=gcna_data.models.land_id, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='visit',
            name='Worker_ID_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
