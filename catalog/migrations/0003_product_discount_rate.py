# Generated by Django 4.0.10 on 2023-05-13 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_rate',
            field=models.IntegerField(blank=True, choices=[(10, 'A'), (20, 'B'), (30, 'C'), (40, 'D'), (50, 'E'), (60, 'F'), (70, 'G')], null=True),
        ),
    ]
