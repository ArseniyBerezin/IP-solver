# Generated by Django 5.0.1 on 2024-01-29 10:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_solver_id_exinsolver_solver_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exinsolver',
            name='solver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.solver'),
        ),
    ]