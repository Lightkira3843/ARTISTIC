# Generated by Django 3.2.19 on 2023-06-23 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='request',
            new_name='rqst',
        ),
    ]