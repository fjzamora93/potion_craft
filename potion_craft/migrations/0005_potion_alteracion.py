# Generated by Django 5.0.3 on 2024-03-26 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potion_craft', '0004_alter_ingrediente_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='potion',
            name='alteracion',
            field=models.CharField(default='psicoactivo', max_length=25),
        ),
    ]