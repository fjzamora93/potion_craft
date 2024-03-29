# Generated by Django 5.0.3 on 2024-03-26 15:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potion_craft', '0002_alter_personaje_esencias_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='esencia',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='ingrediente',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='ingrediente',
            name='esencia',
        ),
        migrations.RemoveField(
            model_name='personaje',
            name='esencias',
        ),
        migrations.RemoveField(
            model_name='personaje',
            name='ingredientes',
        ),
        migrations.RemoveField(
            model_name='personaje',
            name='potions',
        ),
        migrations.RemoveField(
            model_name='potion',
            name='cantidad',
        ),
        migrations.AddField(
            model_name='esencia',
            name='nombre',
            field=models.CharField(default='Esencia', max_length=25),
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='esencias',
            field=models.ManyToManyField(related_name='esencias_por_ingredientes', to='potion_craft.esencia'),
        ),
        migrations.AlterField(
            model_name='esencia',
            name='tipo',
            field=models.CharField(help_text='aire / agua / fuego / tierra', max_length=25),
        ),
        migrations.CreateModel(
            name='PersonajeEsencias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('esencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='potion_craft.esencia')),
                ('personaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='potion_craft.personaje')),
            ],
        ),
        migrations.CreateModel(
            name='PersonajeIngredientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('ingrediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='potion_craft.ingrediente')),
                ('personaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='potion_craft.personaje')),
            ],
        ),
        migrations.CreateModel(
            name='PersonajePotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('personaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='potion_craft.personaje')),
                ('potion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='potion_craft.potion')),
            ],
        ),
    ]
