# Generated by Django 4.0.1 on 2022-02-17 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_specsheet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='specSheet',
            field=models.FileField(blank=True, max_length=1024, upload_to=''),
        ),
    ]