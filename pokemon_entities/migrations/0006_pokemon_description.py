# Generated by Django 5.1.7 on 2025-03-25 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_pokemonentity_defence_pokemonentity_health_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.CharField(default='default description', max_length=1000),
        ),
    ]
