# Generated by Django 2.2 on 2020-08-29 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0011_auto_20200827_0255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='imagen',
        ),
    ]
