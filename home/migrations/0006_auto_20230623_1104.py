# Generated by Django 3.2.19 on 2023-06-23 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20230623_0432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
    ]
