# Generated by Django 2.1 on 2018-08-21 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_auto_20180820_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='mod_rank',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
