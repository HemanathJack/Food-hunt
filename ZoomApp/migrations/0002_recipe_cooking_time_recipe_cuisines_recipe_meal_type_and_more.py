# Generated by Django 4.2.1 on 2023-08-30 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZoomApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recipe',
            name='cuisines',
            field=models.CharField(choices=[('Italian', 'Italian'), ('Indian', 'Indian'), ('Chinese', 'Chinese'), ('Mexican', 'Mexican')], default='Indian', max_length=20),
        ),
        migrations.AddField(
            model_name='recipe',
            name='meal_type',
            field=models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Snack', 'Snack'), ('Dessert', 'Dessert')], default='Breakfast', max_length=20),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='steps',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
