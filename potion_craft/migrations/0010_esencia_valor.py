# Generated by Django 5.0.3 on 2024-04-02 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potion_craft', '0009_personaje_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='esencia',
            name='valor',
            field=models.CharField(default='0', max_length=1),
        ),
    ]