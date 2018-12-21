# Generated by Django 2.1.4 on 2018-12-21 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0060_companion_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='companion',
            name='tipe',
            field=models.CharField(choices=[('K', 'Kavat'), ('U', 'Kubrow'), ('S', 'Sentinel')], default='S', max_length=1),
        ),
    ]
