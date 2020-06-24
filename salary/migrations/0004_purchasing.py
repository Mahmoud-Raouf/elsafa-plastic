# Generated by Django 2.2.7 on 2020-06-14 16:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import salary.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200614_1018'),
        ('salary', '0003_auto_20200614_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='purchasing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='إسم المنتج')),
                ('code', models.IntegerField(default=salary.models.random_string, verbose_name='كود المنتج')),
                ('description', models.TextField(verbose_name='وصف المنتج')),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاريخ الإضافة')),
                ('price', models.FloatField(verbose_name='سعر المنتج')),
                ('count', models.FloatField(verbose_name='الكمية')),
                ('typeofproducts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='typeofproducts')),
            ],
            options={
                'verbose_name': 'purchasing',
                'verbose_name_plural': 'purchasings',
            },
        ),
    ]
