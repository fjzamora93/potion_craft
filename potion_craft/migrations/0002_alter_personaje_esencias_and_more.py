# Generated by Django 5.0.3 on 2024-03-26 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potion_craft', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaje',
            name='esencias',
            field=models.ManyToManyField(blank=True, null=True, related_name='personaje_esencia', to='potion_craft.esencia'),
        ),
        migrations.AlterField(
            model_name='personaje',
            name='ingredientes',
            field=models.ManyToManyField(blank=True, null=True, related_name='personaje_ingrediente', to='potion_craft.ingrediente'),
        ),
        migrations.AlterField(
            model_name='personaje',
            name='potions',
            field=models.ManyToManyField(blank=True, null=True, related_name='personaje_potion', to='potion_craft.potion'),
        ),
    ]