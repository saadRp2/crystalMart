# Generated by Django 4.2.5 on 2024-03-05 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_main_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='main_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.main_category'),
        ),
    ]
