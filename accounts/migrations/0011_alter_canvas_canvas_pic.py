# Generated by Django 4.0.4 on 2022-05-30 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_diary_diary_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canvas',
            name='canvas_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
