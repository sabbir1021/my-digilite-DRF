# Generated by Django 4.0.1 on 2022-01-21 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_productsubcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsubcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_category_with_sub_category', to='api.productcategory'),
        ),
    ]
