# Generated by Django 4.2.5 on 2024-04-05 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_billing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billing',
            old_name='addrees',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='billing',
            old_name='addrees1',
            new_name='address1',
        ),
        migrations.AlterField(
            model_name='billing',
            name='notes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='billing',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
