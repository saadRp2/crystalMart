# Generated by Django 5.1.6 on 2025-02-17 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='prize_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size_id',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]
