# Generated by Django 4.0.4 on 2022-05-16 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_diary_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diary',
            old_name='description',
            new_name='diary_description',
        ),
        migrations.RenameField(
            model_name='diary',
            old_name='name',
            new_name='diary_name',
        ),
    ]