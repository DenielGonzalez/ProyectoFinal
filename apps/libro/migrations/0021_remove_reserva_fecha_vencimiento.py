# Generated by Django 2.2 on 2020-10-26 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0020_auto_20201026_0109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='fecha_vencimiento',
        ),
    ]
