# Generated by Django 4.1.5 on 2023-09-18 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_product_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='grade',
            field=models.CharField(default='empty', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='origin',
            field=models.CharField(default='empty', max_length=30),
        ),
    ]
