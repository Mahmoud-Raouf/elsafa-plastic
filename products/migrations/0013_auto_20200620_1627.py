# Generated by Django 2.2.7 on 2020-06-20 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_productmix_detail_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmix',
            name='type3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type3', to='products.ProductMix_Detail', verbose_name='الوصفة الثالثة'),
        ),
        migrations.AlterField(
            model_name='productmix',
            name='type4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type4', to='products.ProductMix_Detail', verbose_name='الوصفة الرابعة'),
        ),
        migrations.AlterField(
            model_name='productmix',
            name='type5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type5', to='products.ProductMix_Detail', verbose_name='الوصفة الخامسة'),
        ),
        migrations.AlterField(
            model_name='productmix_detail',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='سعر الخلطة'),
        ),
    ]
