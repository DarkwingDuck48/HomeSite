# Generated by Django 5.0 on 2023-12-14 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_alter_operation_operation_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operation',
            name='account',
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]
