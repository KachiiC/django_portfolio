# Generated by Django 3.1.1 on 2020-09-17 16:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200917_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
