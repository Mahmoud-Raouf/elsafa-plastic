# Generated by Django 2.2.7 on 2020-06-21 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20200620_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='costroll', to='products.Roll', verbose_name='سعر الخلطة'),
        ),
        migrations.AlterField(
            model_name='product',
            name='roll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Roll', verbose_name='إسم الخلطة'),
        ),
        migrations.AlterField(
            model_name='roll',
            name='cost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProductMixcost', to='products.ProductMix', verbose_name='تكلفة الكيلو'),
        ),
        migrations.AlterField(
            model_name='roll',
            name='productmix',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.ProductMix', verbose_name='إسم الخلطة'),
        ),
    ]
