# Generated by Django 4.2.16 on 2024-10-16 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_generos'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='fk_generos',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.generos'),
        ),
    ]
