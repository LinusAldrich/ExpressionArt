# Generated by Django 4.0.4 on 2022-06-06 05:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0013_alter_canvas_canvas_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canvas',
            name='canvas_pic',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.CreateModel(
            name='Collage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('collage_name', models.CharField(max_length=200, null=True, unique=True)),
                ('collage_pic', models.ImageField(upload_to='images/')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
