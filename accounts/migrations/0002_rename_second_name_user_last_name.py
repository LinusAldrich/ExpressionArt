# Generated by Django 4.0.4 on 2022-05-15 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='second_name',
            new_name='last_name',
        ),
    ]