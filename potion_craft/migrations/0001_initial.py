# Generated by Django 5.0.3 on 2024-03-26 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Esencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=25)),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=25)),
                ('cantidad', models.IntegerField()),
                ('esencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='esencia_en_ingrediente', to='potion_craft.esencia')),
            ],
        ),
        migrations.CreateModel(
            name='Potion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=140)),
                ('cantidad', models.IntegerField()),
                ('esencias', models.ManyToManyField(related_name='esencias_por_pocion', to='potion_craft.esencia')),
            ],
        ),
        migrations.CreateModel(
            name='Personaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('esencias', models.ManyToManyField(related_name='personaje_esencia', to='potion_craft.esencia')),
                ('ingredientes', models.ManyToManyField(related_name='personaje_ingrediente', to='potion_craft.ingrediente')),
                ('potions', models.ManyToManyField(related_name='personaje_potion', to='potion_craft.potion')),
            ],
        ),
    ]
