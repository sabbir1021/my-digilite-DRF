# Generated by Django 4.0.1 on 2022-01-21 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_productgroup_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productgroup',
            name='slug',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]