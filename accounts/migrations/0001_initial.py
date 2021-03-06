# Generated by Django 4.0.4 on 2022-05-15 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, null=True, unique=True)),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('second_name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
