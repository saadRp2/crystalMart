# Generated by Django 4.2.5 on 2024-04-08 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_rename_addrees_billing_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('product_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
